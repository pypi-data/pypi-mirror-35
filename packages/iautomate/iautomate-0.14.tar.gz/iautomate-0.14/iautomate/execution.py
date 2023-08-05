from abstract_resource import AbstractResource


class Execution(AbstractResource):
    def __init__(self, properties, global_variables=None):
        super(Execution, self).__init__(properties, global_variables)

    def run(self):
        self._run_shell_command(self.action)
