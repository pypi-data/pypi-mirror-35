"""
Allows shell (posix, bash, zsh) code to be written and executed as-is, inside of Python code.
"""

from __future__ import print_function

import inspect

from os import linesep
from subprocess import Popen, PIPE
import sys
import time

CMD_PREFIX = 'SHELLWRAP:CMD_START'
CMD_SUFFIX = 'SHELLWRAP:CMD_END'

class ShellWrap(object):
    allowed_shells = {
        'bash': '/bin/bash',
        'sh': '/bin/sh',
        'posix': '/bin/sh',
        'zsh': '/bin/zsh'
    }

    def __init__(self, interpreter):
        if interpreter not in ShellWrap.allowed_shells.keys():
            raise NotImplemented("{} is not a recognized shell".format(interpreter))

        self.process = Popen([ShellWrap.allowed_shells[interpreter]], stdin=PIPE,
                             stdout=PIPE, stderr=PIPE, bufsize=0)

    def get_shell(self):
        return self.shell

    def get_cmd(self):
        return self.execute_cmd_single

    def env(self, name, value):
        self.shell_runner([self.bash_set_var(name, value)])

    def write_to(self, stream, line):
        if line[-1] != linesep:
            line += linesep

        stream.write(line.encode())

    def execute_cmd_single(self, cmd):
        time0 = time.time()
        exitcode, output, err = self.execute_cmd(cmd)
        runtime_ms = time.time() - time0

        return Result(exitcode, output, err, runtime_ms)

    def execute_cmds_timeout(self, cmd, timeout):
        'Executes a command in a subshell and lets it run for `timeout` seconds.'
        cmd = ' ; '.join(cmd)
        wait_cmd = '''
TIMEOUTPID=$!
COUNTER=0
while kill -0 $TIMEOUTPID >/dev/null 2>&1 && [ $COUNTER -lt ${timeout} ]
do
  sleep 1
  let COUNTER=COUNTER+1
done
if kill -0 $TIMEOUTPID >/dev/null 2>&1; then
  kill $TIMEOUTPID
  false # force an error!
else
  wait $TIMEOUTPID
fi
'''
        # Put the series of commands inside () and send everything to background
        # creating a subshell and getting a PID to it.
        prelude = '''
timeout={}
({}) &
'''.format(timeout, cmd)
        wait_cmd = prelude + wait_cmd
        return self.execute_cmd(wait_cmd)

    def execute_cmd(self, cmd):
        '''This method will execute one line of bash, or 1 command.
        Each bash command can return a collection of things:
        * whatever was writen to stdout
        * the last exitcode
        '''
        self.write_to(self.process.stdin, 'echo "{}"'.format(CMD_PREFIX))
        self.write_to(self.process.stdin, cmd) # TODO(mihai): 'exit' needs to be handled differently
        self.write_to(self.process.stdin, 'echo "{}:$?"'.format(CMD_SUFFIX))

        # Process output
        output = ''
        while True:
            # Read each line, stop when no more lines exist
            line = self.process.stdout.readline()
            if len(line) == 0:
                break

            line = line.decode()
            if line.startswith(CMD_PREFIX):
                continue  # first line
            if line.startswith(CMD_SUFFIX):
                break
            output += line

        exitcode = int(line.split(':')[-1])

        # Process err output
        err = ''
        # line = ''
        # if exitcode != 0:
        #     while True:
        #         # This blocks instead of returning an empty line, after the first line is read
        #         # TODO(mihai): Try mechanism detailed in: https://gist.github.com/mckaydavis/e96c1637d02bcf8a78e7
        #         line = self.process.stderr.readline()
        #         if len(line) == 0:
        #             break

        #         line = line.decode()
        #         err += line

        return exitcode, output, err

    def execute_cmds(self, cmds):
        'Execute a list of commands and returns exitcode and stdout.'
        output = ''
        err = ''
        exitcode = 0
        for cmd in cmds:
            exitcode, stdout, stderr = self.execute_cmd(cmd)
            output += stdout
            err += stderr

        return exitcode, output, err

    def shell_runner(self, set_vars, bash_src, unset_vars, **kwargs):
        '''Executes a series of lines of bash script.
        Returns a tuple of exit code, stdout and stderr.'''

        # set variables if needed (discard output)
        time0 = time.time()
        self.execute_cmds(set_vars)

        # execute commands from the function
        if kwargs.get('timeout'):
            exitcode, stdout, stderr = self.execute_cmds_timeout(bash_src, kwargs.get('timeout'))
        else:
            exitcode, stdout, stderr = self.execute_cmds(bash_src)

        # unsets variables
        self.execute_cmds(unset_vars)

        # compute runtime
        runtime_ms = time.time() - time0

        if kwargs.get('suppress_output', True) is False:
            print(stdout, end='')
            sys.stdout.flush()

        return Result(exitcode, stdout, stderr, runtime_ms)

    def bash_set_var(self, name, value):
        # TODO(licorna): what if value is a command to execute?
        return '{}="{}"'.format(name, value)

    def bash_unset_var(self, name):
        return 'unset {}'.format(name)

    def shell(self, **kwargs):
        'Runs the given function inside a bash interpreter.'
        # Read fn "code" (a series of strings)
        # Sets the value of the arguments to the defined values

        def inner(fn):
            source = inspect.getsourcelines(fn)
            bash_src = [x[1:-1] for x in [x.strip() for x in source[0][2:]]]
            defined_args = inspect.getargspec(fn).args

            def wrapper(*passed_args):
                set_vars = [self.bash_set_var(n, v)
                            for n, v in zip(defined_args, passed_args)]
                unset_vars = [self.bash_unset_var(n) for n in defined_args]
                return self.shell_runner(set_vars, bash_src, unset_vars, **kwargs)

            return wrapper

        return inner

class Result(object):
    def __init__(self, exitcode, stdout, stderr, runtime):
        self.exitcode = exitcode
        self.stdout = stdout
        self.stderr = stderr
        self.runtime = runtime

    def succeeded(self):
        return self.exitcode == 0

    def failed(self):
        return not self.succeeded()
