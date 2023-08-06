# coding=utf-8
"""
Module containing the Migrations class that is used to check if there are un-applied migrations in certain directory and to make the migrations.
"""

from pathlib import Path

import yoyo


class Migrations(object):
    """
    Class used to handle the migrations using yoyo.
    """

    def __init__(self, db_connection_string: str, path: str = None):
        path = Path(path)

        self._backend = yoyo.get_backend(db_connection_string)
        self._migrations = yoyo.read_migrations(path.absolute())

    def migrate(self):
        """
        Applies the migrations to the specified database backend.
        """
        with self._backend.lock():
            self._backend.apply_migrations(self._backend.to_apply(self._migrations))

    def check(self) -> bool:
        """
        Check if there are un-applied migrations. Returns True if there are un-applied migrations or False if the database is up to date.
        :return: A boolean value that represents if there are some un-applied migrations.
         :rtype: bool
        """
        return self._backend.to_apply(self._migrations)
