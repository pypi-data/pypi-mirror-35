# coding=utf-8
"""
Module containing cryptographic utilities.
"""
from passlib.context import CryptContext


class PasswordManager(object):
    """
    Hashing utilities for passwords.
    """

    def __init__(self):
        self._context = CryptContext(
            schemes=["pbkdf2_sha256"],
            default="pbkdf2_sha256",
            pbkdf2_sha256__default_rounds=45000
        )

    def encrypt(self, password: str) -> str:
        """
        Method to encrypt the password.
        :param password: The password to encrypt.
         :type password: str
        :return: The encrypted password.
         :rtype: str
        """
        return self._context.hash(password)

    def verify(self, password: str, hashed: str) -> bool:
        """
        Method to verify if the password is correct.
        :param password: The password to verify.
         :type password: str
        :param hashed: The hash to verify against.
         :type hashed: str
        :return: A boolean value representing if the password is correct.
         :rtype: bool
        """
        return self._context.verify(password, hashed)
