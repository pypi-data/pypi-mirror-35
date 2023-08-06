# coding=utf-8
"""
Environment parser for all kind of projects.
"""
import os


class Parser(object):
    """
    Class to use for getting data from the environment.
    Used to check if the requested keys are available in the environment and to get their
    values or returning an error message for the missing one and exiting the program.
    """

    def __init__(self, ignore_missing: bool = False):
        self._missing = set()
        self._ignore_missing = ignore_missing

    @staticmethod
    def get(item: str, default: object = None) -> object:
        """
        Returns the value from the OS's environment or the default value (specified or None).
        :param item: The key to look for.
        :param default: The default value to use if the key is not found. Default value: None.
         :type default: object
        :return: The value from environment for the specified key.
         :rtype: object
        """
        return os.environ.get(item, default)

    def __getitem__(self, item: str) -> object:
        try:
            return os.environ[item]
        except KeyError as e:
            self._missing.update(e.args)

        return None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None and self._missing and not self._ignore_missing:
            raise SystemExit(f"Missing configuration keys: {self}")

    def __iter__(self):
        for key in self._missing:
            yield key

    def __str__(self):
        return ", ".join(self)
