from abstract_resource import AbstractResource


class Directory(AbstractResource):
    def __init__(self, properties, global_variables=None):
        super(Directory, self).__init__(properties, global_variables)

    def run(self):
        pass