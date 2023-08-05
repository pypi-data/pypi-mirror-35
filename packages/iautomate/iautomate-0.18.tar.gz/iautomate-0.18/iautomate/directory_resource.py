from abstract_resource import AbstractResource


class DirectoryResource(AbstractResource):
    def __init__(self, properties, global_variables=None):
        super(DirectoryResource, self).__init__(properties, global_variables)

    def run(self):
        pass