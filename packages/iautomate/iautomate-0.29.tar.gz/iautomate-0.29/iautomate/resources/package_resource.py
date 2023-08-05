from ..helpers import package_helper
from . import abstract_resource


class PackageResource(abstract_resource.AbstractResource):
    def __init__(self, properties, global_variables=None):
        super(PackageResource, self).__init__(properties, global_variables)
        self.version = properties.get('version', None)

    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, version):
        self.__version = version

    # determine if the version needs to be appended to the command
    def __package_version(self):
        if self.version is None or self.version == 'latest':
            return ''
        else:
            return '=' + self.version

    def run(self):
        if self.action == 'install':
            if package_helper.PackageHelper.is_package_installed(self.name) is True:
                print('Ignoring installing *' + self.name + '*. It is already installed.')
            else:
                self._run_shell_command('apt-get install -y ' + self.name + self.__package_version())
        elif self.action == 'remove':
            if package_helper.PackageHelper.is_package_installed(self.name) is False:
                print('Ignoring removing *' + self.name + '*. It is not installed.')
            else:
                self._run_shell_command('apt-get purge -y --auto-remove ' + self.name)
        else:
            print('Unsupported package action')

        # after_tasks = package.get('after_tasks', None)
        # if after_tasks:
        #     print("Handle after tasks ...")
        #     self.__handle_tasks(after_tasks)
