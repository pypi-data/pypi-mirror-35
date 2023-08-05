import subprocess
import shlex


class ShellHelper(object):
    # run the shell command and print the output if is in debug mode
    @staticmethod
    def run_command(command):
        process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, universal_newlines=True)
        return process.communicate()[0]
