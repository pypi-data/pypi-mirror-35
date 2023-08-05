import unittest
import mock


from iautomate.helpers.shell_helper import ShellHelper


class TestShellHelper(unittest.TestCase):
    @mock.patch('subprocess.Popen')
    def test_run_command(self, mock_subproc_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': ('/to/dummy/dir', 'error')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock

        result = ShellHelper.run_command('pwd')

        self.assertTrue(mock_subproc_popen.called)
        self.assertEquals(result, '/to/dummy/dir')
