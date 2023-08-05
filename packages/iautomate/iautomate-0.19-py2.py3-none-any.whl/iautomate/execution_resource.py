import abstract_resource


class ExecutionResource(abstract_resource.AbstractResource):
    def __init__(self, properties, global_variables=None):
        super(ExecutionResource, self).__init__(properties, global_variables)

    def run(self):
        self._run_shell_command(self.action)
