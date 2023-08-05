import unittest
from collections import OrderedDict

from iautomate.resources.package import Package


class TestAbstractModel(unittest.TestCase):
    def setUp(self):
        self.properties = OrderedDict([('name', 'apache2'), ('action', 'install')])
        self.properties_with_sudo_true = OrderedDict([('name', 'apache2'), ('action', 'install'), ('sudo', True)])
        self.properties_with_sudo_false = OrderedDict([('name', 'apache2'), ('action', 'install'), ('sudo', False)])
        self.global_variables_sudo_true = OrderedDict([('sudo', True), ('debug', True)])
        self.global_variables_sudo_false = OrderedDict([('sudo', False), ('debug', False)])

    def test_properties(self):
        package = Package(self.properties)
        self.assertEquals(package.properties, self.properties)

    def test_name(self):
        package = Package(self.properties)
        self.assertEquals(package.name, 'apache2')

    def test_action(self):
        package = Package(self.properties)
        self.assertEquals(package.action, 'install')

    def test_sudo(self):
        package = Package(self.properties)
        self.assertEquals(package.sudo, None)

        package = Package(self.properties_with_sudo_true)
        self.assertEquals(package.sudo, True)

    def test_global_variables(self):
        package = Package(self.properties)
        self.assertEquals(package.global_variables, None)

        package = Package(self.properties, self.global_variables_sudo_true)
        self.assertEquals(package.global_variables, self.global_variables_sudo_true)

    def test_is_sudo_enabled(self):
        package = Package(self.properties)
        self.assertFalse(package.is_sudo_enabled())

        package = Package(self.properties_with_sudo_true)
        self.assertTrue(package.is_sudo_enabled())

        package = Package(self.properties_with_sudo_false)
        self.assertFalse(package.is_sudo_enabled())

        package = Package(self.properties, self.global_variables_sudo_true)
        self.assertTrue(package.is_sudo_enabled())

        package = Package(self.properties_with_sudo_true, self.global_variables_sudo_true)
        self.assertTrue(package.is_sudo_enabled())

        package = Package(self.properties_with_sudo_false, self.global_variables_sudo_true)
        self.assertFalse(package.is_sudo_enabled())

        package = Package(self.properties_with_sudo_true, self.global_variables_sudo_false)
        self.assertTrue(package.is_sudo_enabled())

        package = Package(self.properties_with_sudo_false, self.global_variables_sudo_false)
        self.assertFalse(package.is_sudo_enabled())

    def test_is_debug_mode(self):
        package = Package(self.properties)
        self.assertFalse(package.is_debug_mode())

        package = Package(self.properties, self.global_variables_sudo_true)
        self.assertTrue(package.is_debug_mode())

        package = Package(self.properties, self.global_variables_sudo_false)
        self.assertFalse(package.is_debug_mode())
