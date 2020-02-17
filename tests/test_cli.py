import click.testing
import pytest

from pipeline_playground import main


@pytest.fixture
def runner():
    return click.testing.CliRunner()


def test_main_succeeds(runner):
    result = runner.invoke(main.main)
    assert result.exit_code == 0
