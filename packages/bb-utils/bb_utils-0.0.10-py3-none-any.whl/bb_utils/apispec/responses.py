# coding=utf-8
"""
Module containing web responses used when api spec specification should be used in the applications.
"""
from typing import Any, Union

from aiohttp.http import RESPONSES
from aiohttp.web_response import Response, json_response
from marshmallow import Schema, ValidationError

from .paginator import ResourcePaginator


class DefaultResponse(object):
    """
    A default successful response to return composed as specified in the api spec specification.
    """

    content_type = "application/vnd.api+json"

    def __init__(self, data: Union[dict, list], *, schema: Schema = None, paginator: ResourcePaginator = None):
        """
        Initializing the response object.
        :param data: The data to be used as response.
         :type data: dict|list
        :param schema: The schema used for validating the data.
         :type schema: Schema
        :param paginator: The paginator to use if needed.
         :type paginator: ResourcePaginator
        """
        if isinstance(data, list):
            assert paginator, "For more than one resource you should specify some paginator to be used."
            self._many = True
        elif isinstance(data, dict):
            assert not paginator, "For a single resource you could not specify a paginator."
            self._many = False
        else:
            raise TypeError("Default resource should be a dictionary or a list of dictionaries.")

        self._validate_schema(data, schema)

        self._data = data
        self._paginator = paginator if paginator else None

    def _validate_schema(self, data: Union[dict, list], schema: Schema = None):
        """
        Validates the data using the specified schema.
        :param data: The data to be validated.
         :type data: dict|list
        :param schema: The schema used in validation.
         :type schema: Schema
        :raises: ValidationError if the validation fails.
        """
        _, errors = schema.load(data, many=self._many) if schema else None, None
        if errors:
            raise ValidationError("You have some invalid fields in your data.", errors=errors)

    @property
    def response(self) -> Response:
        """
        Response getter.
        :return: A web response containing the formatted data.
         :rtype: Response
        """
        body = {"data": self._data}
        if self._paginator:
            body["meta"] = self._paginator.as_dict()
        return json_response(body, content_type=self.content_type)


class ErrorResponse(object):
    """
    An error response containing details about the error occurred (code, title, detailed text).
    """

    content_type = "application/vnd.api+json"

    def __init__(self, errors: Any = None, *, code: int = 400, title: str = RESPONSES[400][0]):
        """
        Initializing the response object.
        :param errors: The errors to report.
         :type errors: Any
        :param code: The status code for the response.
         :type code: int
        :param title: The title of the error response.
         :type title: str
        """
        self._errors = errors
        self._code = code
        self._title = title

    @property
    def response(self) -> Response:
        """
        Response getter.
        :return: A web response containing the formatted error data.
         :rtype: Response
        """
        body = {
            "errors": {
                "status": self._code,
                "title": self._title,
                "details": self._errors or RESPONSES[self._code][1]
            }
        }
        return json_response(body, content_type=self.content_type)
