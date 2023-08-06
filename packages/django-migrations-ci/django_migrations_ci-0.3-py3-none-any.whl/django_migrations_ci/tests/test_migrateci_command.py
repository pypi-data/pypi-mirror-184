import shutil
from pathlib import Path

from django.core.management import execute_from_command_line
from django.db import connections
from django.db.utils import OperationalError
import pytest

from django_migrations_ci import django

CHECKSUM_0001 = "e7cc3570aebddf921af899fc45ba3e9c"
CHECKSUM_0002 = "8c1c0190533e18f1e694d8b0be5c46ad"


def _check_db(connection, suffix=""):
    with django.test_db(connection, suffix=suffix):
        with connection.cursor() as conn:
            conn.execute("SELECT * FROM testapp_bus")
            result = conn.fetchall()
    assert list(result) == [(1, "BUS3R")]


def test_migrateci():
    execute_from_command_line(["manage.py", "migrateci"])
    _check_db(connections["default"])


def test_migrateci_parallel():
    execute_from_command_line(["manage.py", "migrateci", "--parallel", "1"])
    connection = connections["default"]
    _check_db(connection)
    _check_db(connection, suffix="1")
    try:
        _check_db(connection, suffix="2")
    except OperationalError:
        pass
    else:  # pragma: nocover
        pytest.fail("Database 2 should not exist here.")


def test_migrateci_pytest():
    execute_from_command_line(
        [
            "manage.py",
            "migrateci",
            "--parallel",
            "1",
            "--pytest",
        ]
    )
    connection = connections["default"]
    _check_db(connection)
    _check_db(connection, suffix="gw0")
    try:
        _check_db(connection, suffix="gw1")
    except OperationalError:
        pass
    else:  # pragma: nocover
        pytest.fail("Database gw1 should not exist here.")


def test_migrateci_cached(mocker):
    """Apply all cached migrations, no setup needed after that."""
    basepath = Path(__file__).parent
    connection = connections["default"]
    shutil.copyfile(
        basepath / f"dump/0002/{connection.vendor}.sql",
        f"migrateci-default-{CHECKSUM_0002}",
    )
    setup_test_db_mock = mocker.patch("django_migrations_ci.django.setup_test_db")
    execute_from_command_line(["manage.py", "migrateci"])
    setup_test_db_mock.assert_not_called()
    _check_db(connections["default"])


def test_migrateci_cached_partial(mocker):
    """Apply one cached migration and setup after that."""
    basepath = Path(__file__).parent
    connection = connections["default"]
    shutil.copyfile(
        basepath / f"dump/0001/{connection.vendor}.sql",
        f"migrateci-default-{CHECKSUM_0001}",
    )
    setup_test_db_mock = mocker.spy(django, "setup_test_db")
    execute_from_command_line(["manage.py", "migrateci"])
    setup_test_db_mock.assert_called_once()
    _check_db(connections["default"])


def test_migrateci_directory(tmpdir):
    execute_from_command_line(["manage.py", "migrateci", "--directory", str(tmpdir)])
    _check_db(connections["default"])
    assert Path(f"{tmpdir}/migrateci-default-{CHECKSUM_0002}").exists()
