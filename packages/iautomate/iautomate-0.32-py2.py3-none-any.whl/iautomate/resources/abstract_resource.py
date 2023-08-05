from abc import ABCMeta, abstractmethod

from ..helpers import shell_helper


class AbstractResource(object):
    __metaclass__ = ABCMeta

    AFTER_TASKS_KEY = 'after_tasks'

    @abstractmethod
    def __init__(self, properties, global_variables=None):
        self.properties = properties
        self.global_variables = global_variables
        self.name = properties['name']
        self.action = properties.get('action', None)
        self.sudo = properties.get('sudo', None)
        self.after_tasks = properties.get('after_tasks', None)

    @property
    def properties(self):
        return self.__properties

    @properties.setter
    def properties(self, properties):
        self.__properties = properties

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def action(self):
        return self.__action

    @action.setter
    def action(self, action):
        self.__action = action

    @property
    def sudo(self):
        return self.__sudo

    @sudo.setter
    def sudo(self, sudo):
        self.__sudo = sudo

    @property
    def global_variables(self):
        return self.__global_variables

    @global_variables.setter
    def global_variables(self, global_variables):
        self.__global_variables = global_variables

    @property
    def after_tasks(self):
        return self.__after_tasks

    @after_tasks.setter
    def after_tasks(self, after_tasks):
        self.__after_tasks = after_tasks

    @abstractmethod
    def run(self):
        pass

    # check if sudo is enabled
    def is_sudo_enabled(self):
        # if self.sudo exists, it overwrites the global variable
        if self.sudo is True or self.sudo is False:
            return self.sudo

        return True if self.global_variables and self.global_variables.is_sudo_enabled() is True else False

    # run the shell command and print the output if is in debug mode
    def _run_shell_command(self, command):
        # determine sudo
        sudo = 'sudo ' if self.is_sudo_enabled() is True else ''

        output = shell_helper.ShellHelper.run_command(sudo + command)
        if self.global_variables and self.global_variables.is_debug_mode() is True:
            print('* Running: ' + command)

            if output:
                print('** Output: ')
                print(output)

        # make sure there is no whitespace in the output
        return output.strip()
