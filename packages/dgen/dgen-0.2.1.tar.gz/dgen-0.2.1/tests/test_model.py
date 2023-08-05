import unittest
from click.testing import CliRunner
from dgen import cli


COMMAND = 'model'


class TestCommand(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.runner = CliRunner()

    def test_output(self):
        result = self.runner.invoke(cli.main, [COMMAND])
        assert result.exit_code == 0
        assert 'class MyModel(models.Model)' in result.output


class TestNameOption(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.runner = CliRunner()

    def test_option(self):
        result = self.runner.invoke(cli.main, [COMMAND, '--name=Recipe'])
        assert result.exit_code == 0
        assert 'class Recipe(models.Model)' in result.output

    def test_option_short(self):
        result = self.runner.invoke(cli.main, [COMMAND, '-nCompany'])
        assert result.exit_code == 0
        assert 'class Company(models.Model)' in result.output


class TestFieldOption(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.runner = CliRunner()

    def test_option(self):
        result = self.runner.invoke(cli.main, [COMMAND, '--field=t:name'])
        assert result.exit_code == 0

    def test_option_short(self):
        result = self.runner.invoke(cli.main, [COMMAND, '-ft:name'])
        assert result.exit_code == 0

    def test_text_field(self):
        result = self.runner.invoke(cli.main, [COMMAND, '-ft:name'])
        assert 'name = models.TextField(' in result.output
        assert "verbose_name=_('Name')" in result.output

    def test_spaced_verbose_name(self):
        result = self.runner.invoke(cli.main, [COMMAND, '-ft:company_name'])
        assert "verbose_name=_('Company name')" in result.output

    def test_integer_field(self):
        result = self.runner.invoke(cli.main, [COMMAND, '-fi:employee_count'])
        assert 'employee_count = models.IntegerField(' in result.output
        assert "verbose_name=_('Employee count')" in result.output

    def test_boolean_field(self):
        result = self.runner.invoke(cli.main, [COMMAND, '-fb:is_active'])
        assert 'is_active = models.BooleanField(' in result.output
        assert 'default=False,' in result.output
        assert "verbose_name=_('Is active')" in result.output

    def test_date_field(self):
        result = self.runner.invoke(cli.main, [COMMAND, '-fd:start_date'])
        assert 'start_date = models.DateField(' in result.output
        assert "verbose_name=_('Start date')" in result.output

    def test_datetime_field(self):
        result = self.runner.invoke(cli.main, [COMMAND, '-fdt:created'])
        assert 'created = models.DateTimeField(' in result.output
        assert "verbose_name=_('Created')" in result.output

    def test_time_field(self):
        result = self.runner.invoke(cli.main, [COMMAND, '-ftime:refresh_time'])
        assert 'refresh_time = models.TimeField(' in result.output
        assert "verbose_name=_('Refresh time')" in result.output

    def test_email_field(self):
        result = self.runner.invoke(cli.main, [COMMAND, '-fe:email'])
        assert 'email = models.EmailField(' in result.output
        assert "verbose_name=_('Email')" in result.output

    def test_slug_field(self):
        result = self.runner.invoke(cli.main, [COMMAND, '-fs:slug'])
        assert 'slug = models.SlugField(' in result.output
        assert 'allow_unicode=True,' in result.output
        assert "verbose_name=_('Slug')" in result.output

    def test_url_field(self):
        result = self.runner.invoke(cli.main, [COMMAND, '-furl:image_url'])
        assert 'image_url = models.URLField(' in result.output
        assert "verbose_name=_('Image url')" in result.output

    def test_uuid_field(self):
        result = self.runner.invoke(cli.main, [COMMAND, '-fuuid:uuid'])
        assert 'uuid = models.UUIDField(' in result.output
        assert 'unique=True,' in result.output
        assert 'default=uuid.uuid4,' in result.output
        assert 'editable=False,' in result.output
        assert "verbose_name=_('Uuid')" in result.output

    def test_multiple_fields(self):
        result = self.runner.invoke(cli.main, [COMMAND, '-ft:company_name', '-fi:employee_count'])
        assert 'company_name = models.TextField(' in result.output
        assert "verbose_name=_('Company name')" in result.output
        assert 'employee_count = models.IntegerField(' in result.output
        assert "verbose_name=_('Employee count')" in result.output

    def test_fail_without_field_name(self):
        result = self.runner.invoke(cli.main, [COMMAND, '-ft'])
        assert result.exit_code == 2
        assert 'field needs to be in format <type:name>, e.g. t:body' in result.output
