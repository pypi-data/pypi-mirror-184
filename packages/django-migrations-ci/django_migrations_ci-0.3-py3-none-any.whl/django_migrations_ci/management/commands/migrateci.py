import logging

from django.core.files.storage import get_storage_class
from django.core.management.base import BaseCommand

try:
    from django.test.runner import get_max_test_processes
except ImportError:
    # Django<4
    def get_max_test_processes():
        raise Exception(
            "Django<4 do not implement get_max_test_processes."
            " Use --parallel $(nproc) to not depend on this."
        )


from django_migrations_ci import django

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("-n", "--parallel", default=None)
        parser.add_argument(
            "--pytest",
            dest="is_pytest",
            action="store_true",
            default=False,
        )
        parser.add_argument("--directory", default="")
        parser.add_argument(
            "--storage-class",
            default="django.core.files.storage.FileSystemStorage",
            type=get_storage_class,
        )
        parser.add_argument("--depth", type=int, default=0)

    def handle(
        self,
        *args,
        parallel,
        is_pytest,
        directory,
        storage_class,
        depth,
        verbosity,
        **options,
    ):
        if parallel == "auto":
            parallel = get_max_test_processes()
        elif parallel is not None:
            parallel = int(parallel)

        if verbosity >= 2:
            logger.info(f"Using storage {storage_class=} on {directory=}.")
        storage = storage_class(location=directory)

        _, files = storage.listdir("")
        files = set(files)
        if verbosity >= 3:
            logger.info(f"Files in storage: {files}")

        unique_connections = django.get_unique_connections()

        current_checksum = None
        checksums = django.hash_files(depth)
        for cached_checksum in checksums:
            # Current checksum is the first result returned from hash_files.
            if current_checksum is None:
                current_checksum = cached_checksum
                if verbosity:
                    logger.info(f"Migrations current checksum is {current_checksum}.")

            cached_files = {
                connection.alias: f"migrateci-{connection.alias}-{cached_checksum}"
                for connection in unique_connections
            }
            if all(f in files for f in cached_files.values()):
                if verbosity:
                    logger.info(
                        f"Migrations cache found with checksum {cached_checksum}."
                    )
                if verbosity >= 3:
                    for other_checksum in checksums:
                        logger.info(
                            f"Calculated checksum {other_checksum} not evaluated."
                        )
                break

            if verbosity >= 2:
                logger.info(
                    f"Migrations cache NOT found for checksum {cached_checksum}."
                )

        else:
            cached_checksum = None
            cached_files = None
            if verbosity:
                logger.info("Database cache does not exist.")

        if cached_files:
            if verbosity >= 2:
                logger.info("Create test db from cache.")
            django.create_test_db(verbosity=verbosity)
            for connection in unique_connections:
                cached_file = cached_files[connection.alias]
                with django.test_db(connection):
                    django.load(connection, cached_file, storage)

        if current_checksum != cached_checksum:
            if verbosity >= 2:
                logger.info(
                    f"Setup test db from {cached_checksum=} to {current_checksum=}."
                )

            django.setup_test_db(verbosity=verbosity)
            for connection in unique_connections:
                current_file = f"migrateci-{connection.alias}-{current_checksum}"
                with django.test_db(connection):
                    django.dump(connection, current_file, storage)

        if parallel:
            if verbosity >= 2:
                logger.info(f"Clone test db for {parallel=}.")
            for connection in unique_connections:
                with django.test_db(connection):
                    django.clone_test_db(
                        connection=connection,
                        parallel=parallel,
                        is_pytest=is_pytest,
                        verbosity=verbosity,
                    )
