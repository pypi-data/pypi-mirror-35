# coding=utf-8
"""
Base views with functionality for aiohttp requests.
"""
from aiohttp.web import Request, View


class MissingHeadersException(Exception):
    """
    Exception raised when some headers are missing from the request made at the server.
    """
    pass


class HeadersCheck(object):
    """
    Class that holds the logic for checking if there are some missing headers in the request.
    """

    @staticmethod
    def check_for_missing_headers(*headers):
        """
        Check if there are some missing headers in the request.
        :param headers: The headers to check for.
         :type headers: list
        :return: The decorator for the method.
         :rtype: function
        """

        def decorator(func):
            """
            The decorator method.
            :param func: The decorated function.
             :type func: function
            :return: The wrapper for the method.
             :rtype: function
            """

            def wrapper(obj, *args, **kwargs):
                """
                Checks if there are missing headers in the request.
                :param obj: A Request or a View object.
                 :type obj: Request|View
                :param args: Arguments.
                 :type args: list
                :param kwargs: Keyword arguments.
                 :type kwargs: dict
                :return: The result from calling the method if all the headers are in place.
                 :rtype: object
                :raises: TypeError, MissingHeadersException
                """
                if isinstance(obj, View):
                    request = obj.request
                elif isinstance(obj, Request):
                    request = obj
                else:
                    return TypeError("The `check for missing headers` decorated method should have a Request or a View as first parameter.")

                missing = set()
                for header in headers:
                    if header not in request.headers:
                        missing.update([header])
                if missing:
                    missing = ", ".join(missing)
                    raise MissingHeadersException(f"Missing headers: [{missing}].")

                return func(obj, *args, **kwargs)

            return wrapper

        return decorator
