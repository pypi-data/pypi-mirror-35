from abstract_resource import AbstractResource


class File(AbstractResource):
    def __init__(self, properties, global_variables=None):
        super(File, self).__init__(properties, global_variables)

    def run(self):
        pass