"""
Defines the console host and support classes.
"""
import shutil
import sys
from os import system
from typing import List, Optional, TypeVar, Dict

import builtins

import re

from intermake.engine import cli_helper, constants
from intermake.engine.async_result import AsyncResult
from intermake.engine.constants import EDisplay, EStream
from intermake.engine.environment import MCMD
from intermake.engine.host_manager import RunHost
from intermake.engine.mandate import Mandate
from intermake.engine.abstract_command import AbstractCommand
from intermake.engine.progress_reporter import IProgressReceiver, QueryInfo, UpdateInfo
from intermake.engine.theme import Theme
from intermake.hosts.base import ERunMode, AbstractHost, ERunStatus
from intermake.visualisables.visualisable import VisualisablePath

from mhelper import MEnum, exception_helper, file_helper, string_helper, ansi_helper, ArgInspector, ArgsKwargs
from mhelper.comment_helper import override
from mhelper.exception_helper import SwitchError

#
# CONSTANTS
#
from mhelper.special_types import NOT_PROVIDED
from mhelper.string_helper import FindError


# Characters
_CHAR_PROGRESS_SIDE_LEFT = Theme.PROGRESS_COLOUR_PROGRESS_SIDE + "▐"
_CHAR_PROGRESS_SIDE_RIGHT = Theme.PROGRESS_COLOUR_PROGRESS_SIDE + "▌"
_CHAR_PROGRESS_SPACE_LEFT = " "
_CHAR_PROGRESS_SPACE_RIGHT = " "
_CHAR_PROGRESS_POINT = "▌"
_CHAR_PROGRESS_POINT_BOUNCY = "•••"

T = TypeVar( "T" )


class EConsoleReport( MEnum ):
    """
    Progress report types.
    
    :cvar SILENT: No reports
    :cvar ANSIART: Draw graphical loading
    :cvar SIMPLE: Literal dump of progress reports
    :cvar MESSAGES: Only display messages, not generic progress updates
    """
    SILENT = 0
    ANSIART = 1
    SIMPLE = 2
    MESSAGES = 3


class _ConsoleHostSettings:
    """
    User specified settings for the console host.
    Changes persist between sessions.
    
    :ivar console_width_override : Specifies the width of console.
                                   If this is zero (the default) the system is queried.
                                   This setting is used for word wrap and is not always respected.
    :ivar clear_screen           : When set, the console display is cleared between command executions.
    :ivar force_echo             : When set, commands are repeated back to the user.
                                   This is applied even if the user did not invoke the command themselves.
    :ivar remove_ansi            : When set, ANSI colour codes are stripped from the output.
                                   This only applies to output relayed through Intermake, application specific
                                   output may not respect this setting.
    :ivar hide_streams           : When set, streams are no longer shown to the left of the messages displayed in the
                                   console.
    :ivar remove_utf             : When set, non-ASCII sequences are substituted in the output.
                                   This only applies to output relayed through Intermake, application specific
                                   output may not respect this setting.
    :ivar show_external_streams  : Show output from running external applications.
    """
    
    
    def __init__( self ) -> None:
        self.console_width_override: int = 0
        self.clear_screen: bool = False
        self.force_echo: bool = False
        self.remove_ansi: bool = False
        self.hide_streams: bool = False
        self.remove_utf: bool = False
        self.show_external_streams: bool = False


class ConsoleHostConfiguration:
    """
    System defined settings for the console host.
    These are reset on host instantiation and changes do not persist between sessions.
    
    :ivar force_echo           : Echo commands
    :ivar report               : Reporting mode
    :ivar use_dot              : Use `.` instead of `_`
    :ivar cluster_index        : Index for compute clusters
    :ivar cluster_count        : Count for compute clusters
    :ivar run_mode:            : Default options set chosen
    """
    
    
    def __init__( self, run_mode: ERunMode ):
        if run_mode not in (ERunMode.ARG, ERunMode.CLI, ERunMode.PYI, ERunMode.PYS, ERunMode.JUP):
            raise SwitchError( "run_mode", run_mode, details = "This run-mode is not supported by ConsoleHost. Did you mean to use a different host?" )
        
        self.run_mode = run_mode
        self.report = EConsoleReport.ANSIART
        self.use_dot = bool( run_mode in (ERunMode.ARG, ERunMode.CLI) )
        self.cluster_index = 0
        self.cluster_count = 1
        self.force_echo = False
    
    
    def __str__( self ) -> str:
        return "ConsoleHost({})".format( self.run_mode )


RX1 = re.compile( r"[^\x00-\x7F]" )


class ConsoleHost( AbstractHost, IProgressReceiver ):  # this host is always single-threaded so it acts as its own progress receiver
    """
    Hosts commands in CLI mode
    """
    
    
    def __init__( self, config: ConsoleHostConfiguration ):
        """
        CONSTRUCTOR
        See the `Core.initialise` function for parameter descriptions.
        """
        super().__init__()
        self.__configuration = config
        self.__settings = None
        self.__pulse = False
        self.__last_message_id = None  # type: Optional[List[int]]
        self.__last_info_depth = None
        self.__last_info_thread_index = None
        self.__browser_path = None
        self.__mandates = []
        self.__last_stream = None
        self.__bouncy_current = 0
        self.__bouncy_delta = 1
    
    
    def on_get_can_return( self ):
        return self.console_configuration.run_mode != ERunMode.ARG
    
    
    def on_status_changed( self, status: ERunStatus ):
        if self.console_configuration.run_mode == ERunMode.JUP and status == ERunStatus.STOP:
            self._print( "The Jupyter host cannot be stopped without exiting the application. The application will now exit." )
            exit( 1 )
    
    
    def __str__( self ) -> str:
        return str( self.console_configuration )
    
    
    def _print( self, text, end = "\n" ):
        if self.console_settings.remove_ansi:
            text = ansi_helper.without_ansi( text )
        
        if self.console_settings.remove_utf:
            text = RX1.sub( ".", text )
        
        print( text, end = end, file = sys.stderr )
    
    
    @classmethod
    def get_default( cls, run_mode: ERunMode ):
        return cls( ConsoleHostConfiguration( run_mode ) )
    
    
    def on_get_console_width( self ) -> int:
        # Unpickling settings can cause errors, when these errors get printed, they loop back here, hence we avoid the loop by not forcing an unpickle of the settings at this stage
        if self.__settings is not None:
            if self.__settings.console_width_override > 0:
                return self.__settings.console_width_override
        
        return max( 10, shutil.get_terminal_size()[0] - 5 )  # -1 because the last character causes a newline, -4 for the stream sidebar
    
    
    def on_translate_name( self, name: str ) -> str:
        return self.translate_name_mode( name, self.__configuration.use_dot )
    
    
    @staticmethod
    def translate_name_mode( name: str, use_dot: bool ):
        char = "." if use_dot else "_"
        text = str( name )
        
        for x in " _-.()":
            text = text.replace( x, char )
        
        for x in "\"'":
            text = text.replace( x, "" )
        
        charchar = char + char
        
        while charchar in text:
            text = text.replace( charchar, char )
        
        text = text.lower()
        
        return text
    
    
    @override
    def on_run_host( self, args: RunHost ):
        """
        Runs the host's main loop.
        """
        run_mode = self.console_configuration.run_mode
        
        # if self.console_settings.clear_screen:
        #     from intermake.commands.common_commands import cls
        #     cls()
        
        if run_mode == ERunMode.ARG:
            from intermake.hosts.frontends.command_line import start_cli
            start_cli( True )
        elif run_mode == ERunMode.CLI:
            from intermake.hosts.frontends.command_line import start_cli
            start_cli( False )
        elif run_mode == ERunMode.PYI:
            import code
            from intermake.hosts.frontends.command_line import INTERMAKE_PROMPT
            sys.ps1 = INTERMAKE_PROMPT
            code.interact( banner = cli_helper.format_banner( "Python Interactive", "help()", "cmdlist()" ), local = self.__get_pyi_dict() )
        elif run_mode == ERunMode.JUP:
            builtins.__dict__.update( self.__get_pyi_dict() )  # TODO: This isn't great, how do we get out of it?
            MCMD.print( cli_helper.format_banner( "Jupyter Interactive", "help()", "cmdlist()", full = True ) )
            args.persist = True
        elif run_mode == ERunMode.PYS:
            args.persist = True
        else:
            raise SwitchError( "run_mode", run_mode )
    
    
    def __get_pyi_dict( self ) -> Dict[str, object]:
        """
        Returns a dictionary of the commands wrapped in "_PyiCommandWrapper" instances.
        """
        from intermake.engine.abstract_command import AbstractCommand
        
        r: Dict[str, AbstractCommand] = { }
        
        # Names to avoid overriding, we don't want to override `exit` but we do want to
        # override `help`.
        avoid = [x for x in dir( builtins ) if not x.startswith( "_" )]
        avoid.remove( "help" )
        
        for command in self.environment.commands:
            assert isinstance( command, AbstractCommand )
            
            for n in command.names:
                if n in avoid:
                    n = MCMD.environment.abv_name.lower() + "_" + n
                
                r[n] = _PyiCommandWrapper( command )
        
        return r
    
    
    def on_get_help_message( self ) -> str:
        if self.console_configuration.run_mode == ERunMode.ARG:
            return """
            Welcome to $(APPNAME). You are in command line arguments (ARG) mode.
            
            Usage:
                `$(APPNAME) "commands"`
                
            To see the list of commands type:

                `$(APPNAME) cmdlist`
                
            Or to run the `eggs` command:
            
                `$(APPNAME) eggs`
                
            (all commands can be abbreviated so you can also use `$(APPNAME) egg`)

            You can use `?` to get help on a command:

                `$(APPNAME) eggs?`
                
            (you can also use `$(APPNAME) ?eggs` or `$(APPNAME) help eggs`)

            See that "eggs" takes two arguments, "name" and "good".
            
            You can specify the arguments after the command:

                `$(APPNAME) eggs Humpty True`
                
            If it's complex, you can put your command in quotes so as not to confuse your terminal:
            
                `$(APPNAME) "eggs Humpty True"`

            You can name the arguments:

                `$(APPNAME) "eggs good=True"`

            You can also use `?` to get help on the last argument:

                `$(APPNAME) "eggs name?"`
                
            This works for quick reference, if you are busy typing a command:
            
                `$(APPNAME) "eggs name=Humpty good?"`

            Specify `+` to quickly set boolean arguments:

                `$(APPNAME) "eggs +good"`
                
            (you can abbreviate all arguments, so you can just use `$(APPNAME) eggs +g`)

            You should use more quotes to pass parameters with spaces:

                `$(APPNAME) "eggs 'Humpty Dumpty'"`
                
            For the list of commands type:
            
                `$(APPNAME) cmdlist`
                
            To start the UI:
            
                `$(APPNAME) cli`
                
            Use ` : ` (surrounded with spaces) to pass multiple commands
            
                `$(APPNAME) cmdlist : cli`
                
            You can substitute ` : ` for ` then `, if `:` confuses your command line.

            If you don't specify any commands, the CLI UI will start automatically.
            """
        elif self.console_configuration.run_mode == ERunMode.CLI:
            return """
            Welcome to $(APPNAME). You are in command line interactive (CLI) mode.
            
            To see the list of commands type:
            
                `cmdlist`

            To run a command just type it, e.g. for the "eggs" command:

                `eggs`
                
            (You can abbreviate all commands, so you can also type `egg`)

            You can use `?` to get help on a command:

                `eggs?`
                
            (You can also type `?eggs` or `help eggs`)

            See that "eggs" takes two arguments, "name" and "good".
            
            You can specify the arguments after the command:

                `eggs Humpty True`

            You can also name the arguments:

                `eggs good=True`

            You can also use `?` to get help on the last argument:

                `eggs name?`

            Specify `+` to quickly set boolean arguments:

                `eggs +good`
                
            (you can abbreviate all arguments, so you can just use `eggs +g`)
            
            To pass multiple commands on the same line use ` : ` (surrounded with spaces)
            
                `eggs Tweedledum : eggs Tweedledee` 

            You should use quotes to pass parameters with spaces:

                `eggs "Humpty Dumpty"`
            """
        elif self.console_configuration.run_mode == ERunMode.PYI:
            return """
            Welcome to $(APPNAME). You are in Python interactive (PYI) mode.
            
            Run the `cmdlist` function to get the list of $(APPNAME) features.
            
                `cmdlist()`

            The $(APPNAME) commands have already been imported, for instance to run $(APPNAME)'s `eggs` command:

                `eggs()`

            The $(APPNAME)'s commands have been imported as objects, so you can use .help() for help:

                `eggs.help()`

            See that `eggs` takes two arguments, `name` and `good`.
            
            You can specify arguments like so:

                `eggs("Humpty", True)`

            Or you can name them:

                `eggs(name = "Humpty", good = True)`
                
            For help on Python specifics, invoke the standard Python help via:
            
                `python_help()`
            """
        elif self.console_configuration.run_mode == ERunMode.JUP:
            return """
            Welcome to $(APPNAME). You are in Jupyter (JUP) mode.
            
            Run the `cmdlist` function to get the list of $(APPNAME) features.
            
                `cmdlist()`

            The $(APPNAME) commands have already been imported, for instance to run $(APPNAME)'s `eggs` command:

                `eggs()`

            The $(APPNAME)'s commands have been imported as objects, so you can use .help() for help:

                `eggs.help()`

            See that `eggs` takes two arguments, `name` and `good`.
            
            You can specify arguments like so:

                `eggs("Humpty", True)`

            Or you can name them:

                `eggs(name = "Humpty", good = True)`
            """
        elif self.console_configuration.run_mode == ERunMode.PYS:
            return """
            Welcome to $(APPNAME). You are in Python scripting (PYS) mode.
            
            This is the same as Python interactive mode, but nothing has been imported
            for you, and providing an interface - if any - is down to the developer.
            
            Use $(APPNAME) as any other Python library, for instance to get the complete
            list of features:

                `from  $(APPNAME) import common_commands`
                `common_commands.cmdlist()`

            Or to run the "eggs" command:

                `from  $(APPNAME) import common_commands`
                `common_commands.eggs()`

            Most $(APPNAME) commands are objects, so to access their help:
            
                `common_commands.eggs.help()` 
                
            Please see the Python documentation for more details.
            """
        else:
            return super().on_get_help_message()
    
    
    @property
    def console_configuration( self ) -> ConsoleHostConfiguration:
        return self.__configuration
    
    
    @property
    def console_settings( self ) -> _ConsoleHostSettings:
        if self.__settings is None:
            if self.environment is None:
                return _ConsoleHostSettings()  # usually only occurs if _all_ warnings are enabled
            
            self.__settings = self.environment.local_data.store.bind( "console", _ConsoleHostSettings() )
        
        # noinspection PyTypeChecker
        return self.__settings
    
    
    @property
    def browser_path( self ) -> VisualisablePath:
        if self.__browser_path is None:
            self.__browser_path = VisualisablePath.get_root()
        
        return self.__browser_path
    
    
    @browser_path.setter
    def browser_path( self, value ) -> None:
        self.__browser_path = value
    
    
    @override
    def on_command_execute( self, command: AbstractCommand, args: ArgsKwargs, host_args: ArgsKwargs ) -> AsyncResult:
        """
        OVERRIDE
        CLI mode:
        * Invokes the plugin in the current thread, this means it can return the result verbatim as well.
        * Raises exceptions in case of error, since everything is verbatim
        """
        host = MCMD.host
        
        if self.console_settings.clear_screen:
            if file_helper.is_windows():
                system( "cls" )
            else:
                system( "clear" )
            
            echo = True
        elif self.console_settings.force_echo or self.console_configuration.force_echo:
            echo = True
        else:
            echo = False
        
        if echo:
            msg = [Theme.COMMAND_NAME + host.translate_name( command.name ) + Theme.RESET]
            
            for arg in command.args:
                value = arg.extract( *args.args, **args.kwargs )
                assert isinstance( arg, ArgInspector )
                name = Theme.ARGUMENT_NAME + arg.name + Theme.RESET
                val_str = Theme.VALUE + str( value ) + Theme.RESET
                
                if " " in val_str or "\"" in val_str:
                    msg.append( Theme.ARGUMENT_NAME + " \"" + name + "=" + val_str + "\"" + Theme.RESET )
                else:
                    msg.append( Theme.ARGUMENT_NAME + " " + name + "=" + val_str + Theme.RESET )
            
            msg.append( Theme.RESET )
            
            self.print_message( "".join( msg ), EStream.ECHO )
        
        mandate = Mandate( host, self, command.name, self.__configuration.cluster_index, self.__configuration.cluster_count, 0.1 )
        
        async_result = AsyncResult( host = self,
                                    command = command,
                                    args = args )
        
        try:
            self.__mandates.append( mandate )
            
            try:
                result = self.handle_command_execute( command, args )
            finally:
                self.end_progress_bar()
                self.__mandates.pop( -1 )
        except BaseException as ex:
            async_result.set_error( exception = ex,
                                    stacktrace = exception_helper.get_traceback(),
                                    messages = mandate.get_message_records() )
            raise
        else:
            async_result.set_result( result = result,
                                     messages = mandate.get_message_records() )
        
        return async_result
    
    
    def end_progress_bar( self ) -> None:
        """
        If the console cursor is still at the end of a progress bar, be done with it and finish the line.
        """
        if self.__last_message_id is not None:
            sys.stdout.write( "⏎\n" )
            sys.stdout.flush()
            self.__last_message_id = None
        else:
            sys.stdout.flush()
    
    
    def print_message( self, message: str, stream: EStream = EStream.PROGRESS ):
        """
        Calling the inbuilt `print` won't place the newline at the end of any progress bar, so we use this to print things in CLI mode.
        This is for internal use only. Plugins should use `MCMD.print` to allow printing in other hosts (e.g. GUI) also.
        """
        if self is not None:
            self.end_progress_bar()
        
        if stream == EStream.EXTERNAL_STDERR or stream == EStream.EXTERNAL_STDOUT or stream == EStream.VERBOSE:
            if not self.console_settings.show_external_streams:
                return
        
        message = str( message )
        
        prefix, prefix_s, suffix = self.__get_message_style( stream )
        lines = message.split( "\n" )
        
        for index, line in enumerate( lines ):
            if index == 0:  # and (self is None or self.__last_stream != stream)
                self._print( prefix + line + suffix )
            else:
                self._print( prefix_s + line + suffix )
        
        if self is not None:
            self.__last_stream = stream
        
        sys.stderr.flush()
    
    
    def __get_message_style( self, stream: EStream ):
        if self.console_settings.hide_streams:
            return "", "", ""
        
        if stream == EStream.INFORMATION:
            prefix = constants.INFOLINE_INFORMATION
            prefix_s = constants.INFOLINE_INFORMATION_CONTINUED
            suffix = ""
        elif stream == EStream.PROGRESS:
            prefix = constants.INFOLINE_MESSAGE
            prefix_s = constants.INFOLINE_MESSAGE_CONTINUED
            suffix = ""
        elif stream == EStream.WARNING:
            prefix = constants.INFOLINE_WARNING + Theme.WARNING + "⚠️ "
            prefix_s = constants.INFOLINE_WARNING_CONTINUED + Theme.WARNING + "⚠️ "
            suffix = Theme.RESET
        elif stream == EStream.ECHO:
            prefix = constants.INFOLINE_ECHO
            prefix_s = constants.INFOLINE_ECHO_CONTINUED
            suffix = ""
        elif stream == EStream.SYSTEM:
            prefix = constants.INFOLINE_SYSTEM
            prefix_s = constants.INFOLINE_SYSTEM_CONTINUED
            suffix = ""
        elif stream == EStream.ERROR:
            prefix = constants.INFOLINE_ERROR
            prefix_s = constants.INFOLINE_ERROR_CONTINUED
            suffix = ""
        elif stream == EStream.EXTERNAL_STDOUT:
            prefix = constants.INFOLINE_EXTERNAL_STDOUT
            prefix_s = constants.INFOLINE_EXTERNAL_STDOUT_CONTINUED
            suffix = ""
        elif stream == EStream.EXTERNAL_STDERR:
            prefix = constants.INFOLINE_EXTERNAL_STDERR
            prefix_s = constants.INFOLINE_EXTERNAL_STDERR_CONTINUED
            suffix = ""
        elif stream == EStream.VERBOSE:
            prefix = constants.INFOLINE_VERBOSE
            prefix_s = constants.INFOLINE_VERBOSE_CONTINUED
            suffix = ""
        else:
            raise SwitchError( "stream", stream )
        
        return prefix, prefix_s, suffix
    
    
    @override  # IProgressReceiver
    def question( self, query: QueryInfo ) -> object:
        """
        Because it's single threaded, the CLI can just ask the question in the console.
        """
        self.end_progress_bar()
        return self.ask_cli_question( query )
    
    
    @override  # IProgressReceiver
    def progress_update( self, info: UpdateInfo ):
        """
        Progress updates in the CLI get printed direct to the console.
        """
        depth = len( info.depth )
        
        # Don't draw the title card progress indicator
        if depth == 1 and info.message is None:
            return
        
        if self.__configuration.report == EConsoleReport.SILENT:
            return
        elif self.__configuration.report == EConsoleReport.SIMPLE:
            self.__draw_progress_bar_simple( info )
        elif self.__configuration.report == EConsoleReport.ANSIART:
            self.__draw_progress_bar( info )
        elif self.__configuration.report == EConsoleReport.MESSAGES and info.message is not None:
            self.print_message( info.message.message, stream = info.message.stream )
    
    
    def __draw_progress_bar_simple( self, info: UpdateInfo ):
        depth = len( info.depth )
        
        if info.message is not None:
            self.print_message( info.message.message, stream = info.message.stream )  # to std.out
        else:
            indent = constants.INFOLINE_PROGRESS + ("-" * depth if depth > 0 else "")
            indent_s = constants.INFOLINE_PROGRESS_CONTINUED + ("-" * depth if depth > 0 else "")
            
            self._print( indent + " PROGRESS: text    = {}".format( Theme.PROGRESS_SIMPLE + info.text + Theme.RESET ) )
            
            if info.thread_index != self.__last_info_thread_index:
                self._print( indent_s + "         : thread  = {} / {}".format( info.thread_index, info.num_threads ) )
                self.__last_info_thread_index = info.thread_index
            
            if info.value > 0:
                self._print( indent_s + "         : value   = {} / {}".format( info.value, info.max ) )
            
            if info.value_string:
                self._print( indent_s + "         : value$  = {}".format( info.value_string ) )
            
            self._print( indent_s + "         : passed  = {}".format( string_helper.time_to_string_short( info.total_time ) ) )
            
            remain_text = info.format_time( EDisplay.TIME_REMAINING_SHORT )
            
            if remain_text:
                self._print( indent_s + "         : remain  = {}".format( remain_text ) )
        
        sys.stdout.flush()
    
    
    def __draw_progress_bar( self, info: UpdateInfo ):
        if info.message is not None:
            self.print_message( info.message.message, stream = info.message.stream )  # to std.out
            return
        
        #
        # Where to draw
        #
        this_message_id = [info.uid] + [info.thread_index]
        this_message_id.extend( info.depth )
        
        if this_message_id == self.__last_message_id or self.__last_message_id is None:
            # Same source as last message - overwrite existing line
            self._print( "\r", end = "" )
        elif this_message_id == self.__last_message_id[:-1]:
            # Up one level from last message - don't print anything unless there is extra information
            if not info.value and not info.value_string:
                return
        else:
            # Down one level from last message - start a new line
            self.end_progress_bar()
        
        self.__last_message_id = this_message_id
        
        #
        # What to draw
        #
        WIDTH_SEPARATOR = 3
        WIDTH_THREAD = 2
        WIDTH_TIME = 10
        WIDTH_TOTAL = self.console_width - (WIDTH_SEPARATOR * 4) - WIDTH_THREAD - WIDTH_TIME
        WIDTH_TITLE = int( 0.5 * WIDTH_TOTAL )
        WIDTH_CURRENT = int( 0.25 * WIDTH_TOTAL )
        WIDTH_BAR = int( 0.25 * WIDTH_TOTAL )
        WIDTH_BAR_BOUNCY = WIDTH_BAR - 3
        
        # THREAD COLUMN
        if info.num_threads != 1:
            cell_thread = ansi_helper.fix_width( str( info.thread_index ), WIDTH_THREAD ) + Theme.PROGRESS_CHAR_COLUMN_SEPARATOR
        else:
            cell_thread = ""
        
        # TITLE COLUMN
        col_title_text = "▸" * (len( info.depth ) - 1) + info.text
        cell_title = Theme.PROGRESS_COLOUR_TITLE_COLUMN + ansi_helper.fix_width( col_title_text, WIDTH_TITLE ) + " "
        
        # CURRENT COLUMN
        cell_progress = Theme.PROGRESS_COLOUR_CURRENT_COLUMN + " " + ansi_helper.fix_width( info.format_progress(), WIDTH_CURRENT ) + " "
        
        _colour_progress_left = Theme.PROGRESS_COLOUR_PROGRESS_SPACE_LEFT_ARRAY[len( info.depth ) % len( Theme.PROGRESS_COLOUR_PROGRESS_SPACE_LEFT_ARRAY )]
        
        # BAR COLUMN
        if info.max > 0:
            val = int( (info.value / info.max) * WIDTH_BAR )
            
            if 0 <= val < WIDTH_BAR:
                # Normal bar
                cell_bar = (Theme.PROGRESS_COLOUR_PROGRESS_SIDE
                            + _CHAR_PROGRESS_SIDE_LEFT
                            + _colour_progress_left
                            + ansi_helper.ljust( str( info.value ), val, _CHAR_PROGRESS_SPACE_LEFT )
                            + Theme.PROGRESS_COLOUR_PROGRESS_POINT
                            + _CHAR_PROGRESS_POINT
                            + Theme.PROGRESS_COLOUR_PROGRESS_SPACE_RIGHT
                            + ansi_helper.rjust( str( info.max - info.value ), WIDTH_BAR - val, _CHAR_PROGRESS_SPACE_RIGHT )
                            + Theme.PROGRESS_COLOUR_PROGRESS_SIDE
                            + _CHAR_PROGRESS_SIDE_RIGHT
                            + Theme.RESET)
            elif val == WIDTH_BAR:
                # Full "done" bar
                cell_bar = (Theme.PROGRESS_COLOUR_CURRENT_COLUMN + ("▒" * (WIDTH_BAR + 2)))
            else:
                # Overfull bar
                val = WIDTH_BAR // 2
                cell_bar = (Theme.PROGRESS_COLOUR_PROGRESS_SIDE
                            + _CHAR_PROGRESS_SIDE_LEFT
                            + _colour_progress_left
                            + ansi_helper.ljust( "?", val, "?" )
                            + Theme.PROGRESS_COLOUR_PROGRESS_POINT
                            + "?"
                            + Theme.PROGRESS_COLOUR_PROGRESS_SPACE_RIGHT
                            + ansi_helper.rjust( "?", (WIDTH_BAR - val), "?" )
                            + Theme.PROGRESS_COLOUR_PROGRESS_SIDE
                            + _CHAR_PROGRESS_SIDE_RIGHT
                            + Theme.RESET)
        else:
            # Bouncy bar
            cell_bar = (Theme.PROGRESS_COLOUR_PROGRESS_SIDE
                        + _CHAR_PROGRESS_SIDE_LEFT
                        + Theme.PROGRESS_COLOUR_PROGRESS_SPACE_RIGHT
                        + (_CHAR_PROGRESS_SPACE_LEFT * self.__bouncy_current)
                        + Theme.PROGRESS_COLOUR_PROGRESS_POINT
                        + _CHAR_PROGRESS_POINT_BOUNCY
                        + Theme.PROGRESS_COLOUR_PROGRESS_SPACE_RIGHT
                        + (_CHAR_PROGRESS_SPACE_LEFT * (WIDTH_BAR_BOUNCY - self.__bouncy_current))
                        + Theme.PROGRESS_COLOUR_PROGRESS_SIDE
                        + _CHAR_PROGRESS_SIDE_RIGHT
                        + Theme.RESET)
            
            self.__bouncy_current += self.__bouncy_delta
            
            if self.__bouncy_current == WIDTH_BAR_BOUNCY or self.__bouncy_current == 0:
                self.__bouncy_delta = -self.__bouncy_delta
                
                # TIME COLUMN
        self.__pulse = not self.__pulse
        
        if 0 < info.max != info.value:
            time_remaining = info.estimate_time()[-1]
            time_remaining_prefix = "-"
        else:
            time_remaining = info.total_time  # time elapsed
            time_remaining_prefix = "+"
        
        time_remaining_text = " " + time_remaining_prefix + string_helper.time_to_string_short( time_remaining, ":" if self.__pulse else " " )
        cell_time = Theme.PROGRESS_COLOUR_TIME_COLUMN + ansi_helper.ljust( time_remaining_text, WIDTH_TIME ) + Theme.RESET
        
        # FORMAT EVERYTHING
        text = constants.INFOLINE_PROGRESS + cell_thread + cell_title + Theme.PROGRESS_CHAR_COLUMN_SEPARATOR + cell_progress + Theme.PROGRESS_CHAR_COLUMN_SEPARATOR + cell_bar + Theme.PROGRESS_CHAR_COLUMN_SEPARATOR + cell_time + Theme.RESET + "  "
        
        # PRINT MESSAGE
        if self.console_settings.remove_ansi:
            text = ansi_helper.without_ansi( text )
        
        self._print( text, end = "" )
        sys.stderr.flush()
    
    
    @override  # IProgressReceiver
    def was_cancelled( self ) -> bool:
        """
        OVERRIDE
        Because it operates in the main thread, progress in the CLI cannot be cancelled externally.
        (However, the user can just press CTRL+C to force an error at any point, we already pick this up and handle it accordingly elsewhere.)
        """
        return False
    
    
    @override
    def on_get_mandate( self ) -> Mandate:
        return self.__mandates[-1] if self.__mandates else self.__system_mandate()
    
    
    def __system_mandate( self ) -> Mandate:
        return Mandate( self, self, "System", 0, 1, 0.1 )
    
    
    def ask_cli_question( self, query: QueryInfo ):
        """
        Asks a question in the CLI.
        :param query: The query 
        :return: Selected option from query.options. 
        """
        prefix = Theme.QUERY_PREFIX + "QUERY<" + Theme.RESET + " "
        message = string_helper.prefix_lines( str( query.message ), prefix + Theme.QUERY_MESSAGE, Theme.RESET )
        
        self._print( message )
        
        
        def ___namer( x ) -> str:
            if x is True:
                return "yes"
            elif x is False:
                return "no"
            elif x is None:
                return "cancel"
            else:
                return MCMD.host.translate_name( str( x ) )
        
        
        message = ""
        
        for i, x in enumerate( query.options ):
            if x == "*" and len( query.options ) == 1:
                continue
            
            if i != 0:
                message += (Theme.QUERY_BORDER + "|" + Theme.RESET)
            
            name = ___namer( x ) if x != "" else "«blank»"
            message += Theme.QUERY_OPTION + name + Theme.RESET
            
            if x == query.default:
                message += "*"
        
        if message:
            self._print( prefix + message )
        
        while True:
            self._print( Theme.QUERY_PROMPT, end = "" )
            the_input = input( "QUERY> " ).lower()
            
            if not the_input:
                if query.default is not NOT_PROVIDED:
                    self._print( Theme.RESET, end = "" )
                    return query.default
            
            try:
                if len( query.options ) == 1 and query.options[0] == "*":
                    return the_input
                
                result = string_helper.find( source = query.options,
                                             search = the_input,
                                             namer = ___namer,
                                             detail = "option" )
                
                self._print( Theme.RESET, end = "" )
                return result
            except FindError:
                self._print( Theme.ERROR + "Invalid option, try again." + Theme.RESET )
                continue


class _PyiCommandWrapper:
    def __init__( self, command: AbstractCommand ):
        self.command = command
    
    
    def __call__( self, *args, **kwargs ):
        from intermake.engine.environment import MCMD
        MCMD.host.acquire( self.command ).run( *args, **kwargs )
    
    
    def __repr__( self ):
        return "This is a command named «{0}». Please type '{0}()' to run this function, or type '{0}.help()' for more information.".format( self.command.name )
    
    
    def help( self ):
        from intermake.engine.environment import MCMD
        MCMD.print( cli_helper.get_details_text( self.command ) )
