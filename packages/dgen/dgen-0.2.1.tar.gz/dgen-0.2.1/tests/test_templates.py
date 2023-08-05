import os
import unittest
from click.testing import CliRunner
from dgen import cli


COMMAND = 'templates'
TEMPLATES_DIR = 'templates_dir'
TEMPLATES = [f'{t}.html' for t in [
    'base',
    'index',
    'list',
    'form',
    'confirm_delete',
    'breadcrumb',
]]
BASE_TEMPLATE_PATH = f'{TEMPLATES_DIR}/base.html'


class TestCommand(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.runner = CliRunner()

    @staticmethod
    def assertTemplates(result, templates_dir_path):
        assert result.exit_code == 0
        assert result.output == f'Templates have been generated to the {templates_dir_path} directory.\n'
        for template in TEMPLATES:
            template_path = os.path.join(templates_dir_path, template)
            assert os.path.isfile(template_path)

    def test_success_with_not_existing_templates_dir(self):
        with self.runner.isolated_filesystem():
            result = self.runner.invoke(cli.main, [COMMAND, TEMPLATES_DIR])
            templates_dir_path = os.path.abspath(TEMPLATES_DIR)
            self.assertTemplates(result, templates_dir_path)

    def test_success_with_existing_templates_dir(self):
        with self.runner.isolated_filesystem():
            templates_dir_path = os.path.abspath(TEMPLATES_DIR)
            os.mkdir(templates_dir_path)
            result = self.runner.invoke(cli.main, [COMMAND, TEMPLATES_DIR])
            self.assertTemplates(result, templates_dir_path)


class TestTitleOption(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.runner = CliRunner()

    def test_default_title_in_base_template(self):
        with self.runner.isolated_filesystem():
            self.runner.invoke(cli.main, [COMMAND, TEMPLATES_DIR])
            with open(BASE_TEMPLATE_PATH) as file:
                assert 'My Project' in file.read()

    def test_given_title_in_base_template(self):
        with self.runner.isolated_filesystem():
            self.runner.invoke(cli.main, [COMMAND, TEMPLATES_DIR, '--title="Dgen Title Test"'])
            with open(BASE_TEMPLATE_PATH) as file:
                assert 'Dgen Title Test' in file.read()
