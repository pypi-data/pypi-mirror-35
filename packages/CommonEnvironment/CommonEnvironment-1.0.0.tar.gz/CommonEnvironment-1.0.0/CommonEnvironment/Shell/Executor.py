# ----------------------------------------------------------------------
# |  
# |  Executor.py
# |  
# |  David Brownell <db@DavidBrownell.com>
# |      2018-07-27 11:06:00
# |  
# ----------------------------------------------------------------------
# |  
# |  Copyright David Brownell 2018.
# |  Distributed under the Boost Software License, Version 1.0.
# |  (See accompanying file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)
# |  
# ----------------------------------------------------------------------
"""Contains the Executor method."""

import os
import subprocess
import sys

from contextlib import contextmanager

import six

from CommonEnvironment.Interface import clsinit
from CommonEnvironment import Process
from CommonEnvironment.Shell import All as AllShells
from CommonEnvironment.Shell.Commands import All as AllCommands
from CommonEnvironment.StreamDecorator import StreamDecorator
from CommonEnvironment import StringHelpers

# ----------------------------------------------------------------------
_script_fullpath = os.path.abspath(__file__) if "python" in sys.executable.lower() else sys.executable
_script_dir, _script_name = os.path.split(_script_fullpath)
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
@contextmanager
def Executor( output_stream=sys.stdout,
              max_title_length=80,
            ):
    """
    Object that makes it easy to write "script" files that work on a variety of different
    operating systems. Rather than writing a bash script and a batch script that are functionally
    equivalent, one can write a single python script that will work in both environments.

    Example:
        with Executor() as ex:
            ex.Message("Hello world")

            ex.Call("python another_script.py")
            ex.Message("We will only see this if the script above is successful")
            ex.Call("python sometimes_fails.py", _exit_on_error=False)
            ex.Message("We will always see this due to 'exit_on_error=False'")

            try:
                ex.Execute("foo.exe")
            except:
                ex.Message("Another way to continue after errors")
    """

    assert max_title_length > 3, max_title_length

    with StreamDecorator(output_stream).DoneManager( line_prefix='',
                                                     prefix="\nResults: ",
                                                     suffix='\n',
                                                   ) as dm:
        shell = AllShells.CurrentShell

        # ----------------------------------------------------------------------
        class StopExecutionException(Exception):
            pass

        # ----------------------------------------------------------------------
        class ExecutorObject(object):

            # ----------------------------------------------------------------------
            def __init__(self):
                for command in AllCommands.ALL_COMMANDS:
                    setattr(self, command.__name__, command)

            # ----------------------------------------------------------------------
            def __call__( self,
                          command_or_commands, 
                          title=None,
                          exit_on_error=True,
                          display=True,
                        ):
                content = shell.GenerateCommands(command_or_commands)

                # ----------------------------------------------------------------------
                def Invoke(done_manager):
                    if display:
                        output_stream = done_manager.stream
                    else:
                        output_stream = six.moves.StringIO()

                    done_manager.result = Process.Execute(content, output_stream)
                    if done_manager.result != 0:
                        if not display:
                            dm.stream.write(output_stream.getvalue())

                        if exit_on_error:
                            raise StopExecutionException()

                # ----------------------------------------------------------------------

                if display:
                    title = title or content
                    if len(title) > max_title_length:
                        title = "{}...".format(title[:max_title_length - 3])

                    dm.stream.write("Executing '{}'...".format(title))
                    with dm.stream.DoneManager() as this_dm:
                        Invoke(this_dm)
                        
                else:
                    Invoke(dm)

        # ----------------------------------------------------------------------
    
        obj = ExecutorObject()

        try:
            yield obj
        except StopExecutionException:
            pass
        except:
            import traceback

            dm.stream.write("ERROR: {}".format(StringHelpers.LeftJustify(traceback.format_exc(), len("ERROR: "))))
            dm.result = -1

    sys.exit(dm.result)

# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
@clsinit
class _ExecutorObject(object):

    _FINISHED_SENTINEL                      = "<!@==+____Finished Sentinel____+==@!>"

    # ----------------------------------------------------------------------
    @classmethod
    def __clsinit__(cls):
        for command in AllCommands.ALL_COMMANDS:
            # ----------------------------------------------------------------------
            def DynamicMethod( self,
                               *args,
                               _display=True,
                               _command=command,
                               **kwargs,
                             ):
                return self._Invoke( _command(*args, **kwargs),
                                     _display=_display,
                                   )

            # ----------------------------------------------------------------------

            setattr(cls, command.__name__, DynamicMethod)

        cls._invoke_suffix = "&& {}".format(AllShells.CurrentShell.GenerateCommands(AllShells.CurrentShell.Commands.Message(cls._FINISHED_SENTINEL), suppress_prefix=True, suppress_suffix=True))
        print("BugBug", cls._invoke_suffix, "\n\n\n\n")

    # ----------------------------------------------------------------------
    def __init__(self, output_stream):
        self._output_stream                 = output_stream
        self._process                       = subprocess.Popen( [ "/bin/bash", ], # BugBug [ "cmd.exe", ],
                                                                stdin=subprocess.PIPE,
                                                                stdout=subprocess.PIPE,
                                                                stderr=subprocess.STDOUT,
                                                                shell=True,
                                                              )
        self._is_closed                     = False

        # BugBug: Explain
        # BugBug while True:
        # BugBug     line = self._process.stdout.readline().strip()
        # BugBug     if not line:
        # BugBug         break

    # ----------------------------------------------------------------------
    def Close(self):
        if self._is_closed:
            return

        # BugBug

        self._is_closed = True
        return self

    # ----------------------------------------------------------------------
    def __enter__(self):
        # Nothing to do here
        pass

    # ----------------------------------------------------------------------
    def __exit__(self):
        return self.Close()

    # ----------------------------------------------------------------------
    def Commands( self,
                  commands,
                  _display=True,
                ):
        return self._Invoke( commands,
                             _display=_display,
                           )

    # ----------------------------------------------------------------------
    def _Invoke( self,
                 command_or_commands,
                 _display,
               ):
        this_output_stream = self._output_stream if _display else six.moves.StringIO()

        pending = []

        # ----------------------------------------------------------------------
        def DisplayProc(content):
            for letter in content:
                if letter == self._FINISHED_SENTINEL[len(pending)]:
                    pending.append(letter)
                    
                    if len(pending) == len(self._FINISHED_SENTINEL):
                        pending[:] = []
                        return False
                    
                    continue

                if pending:
                    this_output_stream.write(''.join(pending))
                    pending[:] = []

                this_output_stream.write(letter)

            return True

        # ----------------------------------------------------------------------

        self._process.stdin.write(bytearray("{}{}\n".format( AllShells.CurrentShell.GenerateCommands(command_or_commands, suppress_prefix=True, suppress_suffix=True),
                                                             self._invoke_suffix, 
        ), "utf-8"))
        self._process.stdin.flush()

        # print("BugBugA")
        Process.ConsumeOutput(self._process.stdout, DisplayProc)
        # print("BugBugB")

obj = _ExecutorObject(sys.stdout)

obj.Set("Foo", "Bar")
obj.Message("This is a test1")
obj.Message("-- $Foo --")
obj.Message("This is a test2")
# print("BugBug", _ExecutorObject(sys.stdout).Message("This is a test"))
# print("BugBug", _ExecutorObject(sys.stdout).CommandPrompt("sakljfjksdafa"))
# print("BugBug", _ExecutorObject(sys.stdout).Message("This is a test2"))
