from package_helper import PackageHelper
from abstract_resource import AbstractResource


class Package(AbstractResource):
    def __init__(self, properties, global_variables=None):
        super(Package, self).__init__(properties, global_variables)
        self.version = properties.get('version', None)
        self.after_tasks = properties.get('after_tasks', None)

    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, version):
        self.__version = version

    @property
    def after_tasks(self):
        return self.__after_tasks

    @after_tasks.setter
    def after_tasks(self, after_tasks):
        self.__after_tasks = after_tasks

    # determine if the version needs to be appended to the command
    def __package_version(self):
        if self.version is None or self.version == 'latest':
            return ''
        else:
            return '=' + self.version

    def run(self):
        if self.action == 'install':
            if PackageHelper.is_package_installed(self.name) is True:
                print('Ignoring installing *' + self.name + '*. It is already installed.')
            else:
                self._run_shell_command('apt-get install -y ' + self.name + self.__package_version())
        elif self.action == 'remove':
            if PackageHelper.is_package_installed(self.name) is False:
                print('Ignoring removing *' + self.name + '*. It is not installed.')
            else:
                self._run_shell_command('apt-get purge -y --auto-remove ' + self.name)
        else:
            print('Unsupported package action')

        # after_tasks = package.get('after_tasks', None)
        # if after_tasks:
        #     print("Handle after tasks ...")
        #     self.__handle_tasks(after_tasks)
