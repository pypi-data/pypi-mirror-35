# coding=utf-8
"""
Paginator class to be used according to the `api spec` specifications.
"""
from typing import Optional


class ResourcePaginator(object):
    """
    Paginates some resources via dictionary objects or url parameters.
    """

    def __init__(self, url: str = None, count: int = 0, limit: int = 20, page: int = 1):
        """
        Initializes the paginator with the necessary information.
        :param url: The base url to append the pagination to.
         :type url: str
        :param count: The total number of resources in the paginator.
         :type count: int
        :param limit: The limit to be used in pagination.
         :type limit: int
        :param page: The current page in paginator.
         :type page: int
        """
        self._url = url if url else ""
        self._count = self._limit = self._page = self._offset = self._pages = 0

        self.reinitialize(count, limit, page)

    @property
    def count(self) -> int:
        """
        Count getter.
        :return: The total number of resources.
         :rtype: int
        """
        return self._count

    @property
    def limit(self) -> int:
        """
        Limit getter.
        :return: The limit used when paginating.
         :rtype: int
        """
        return self._limit

    @property
    def page(self) -> int:
        """
        Page getter.
        :return: The current page.
         :rtype: int
        """
        return self._page

    @property
    def offset(self) -> int:
        """
        Offset getter.
        :return: The current offset.
         :rtype: int
        """
        return self._offset

    @property
    def pages(self) -> int:
        """
        Pages getter.
        :return: The total number of pages with the current configuration.
         :rtype: int
        """
        return self._pages

    def as_url(self, page: bool = False) -> str:
        """
        Get's the current url from the paginator.
        :param page: Specifies if the url contains the page number or the offset.
         :type page: bool
        :return: An URL for the current page.
         :rtype: str
        """
        return "{url}?limit={limit}&{key}={value}".format(
            url=self._url,
            limit=self._limit,
            key="page" if page else "offset",
            value=self._page if page else self._offset
        )

    def as_dict(self, page: bool = False) -> dict:
        """
        Get's the current configuration as dictionary.
        :param page: Specifies if the dictionary contains the page number or the offset.
         :type page: bool
        :return: A dictionary with the paginator's configuration.
         :rtype: dict
        """
        meta = {
            "count": self._count,
            "limit": self._limit
        }
        meta.update({"page": self._page} if page else {"offset": self._offset})
        return meta

    def _go_prev(self) -> bool:
        """
        Decreases the necessary values in order to move to the previous page.
        :return: A boolean value indicating if the movement can be done.
         :rtype: bool
        """
        if self.page < 2:
            return False

        self._page -= 1
        self._offset -= self._limit
        return True

    def prev_url(self, page: bool = False) -> Optional[str]:
        """
        Get's the previous page url from the paginator.
        :param page: Specifies if the url contains the page number or the offset.
         :type page: bool
        :return: An URL for the previous page.
         :rtype: str
        """
        if self._go_prev():
            return "{url}?limit={limit}&{key}={value}".format(
                url=self._url,
                limit=self._limit,
                key="page" if page else "offset",
                value=self._page if page else self._offset
            )
        return None

    def prev_dict(self, page: bool = False) -> Optional[dict]:
        """
        Get's the previous page configuration as dictionary.
        :param page: Specifies if the dictionary contains the page number or the offset.
         :type page: bool
        :return: A dictionary with the paginator's configuration for previous page.
         :rtype: dict
        """
        if self._go_prev():
            meta = {
                "count": self._count,
                "limit": self._limit
            }
            meta.update({"page": self._page} if page else {"offset": self._offset})
            return meta
        return None

    def _go_next(self) -> bool:
        """
        Increases the necessary values in order to move to the next page.
        :return: A boolean value indicating if the movement can be done.
         :rtype: bool
        """
        if self.page >= self.pages:
            return False

        self._page += 1
        self._offset += self._limit
        return True

    def next_url(self, page: bool = False) -> Optional[str]:
        """
        Get's the next page url from the paginator.
        :param page: Specifies if the url contains the page number or the offset.
         :type page: bool
        :return: An URL for the next page.
         :rtype: str
        """
        if self._go_next():
            return "{url}?limit={limit}&{key}={value}".format(
                url=self._url,
                limit=self._limit,
                key="page" if page else "offset",
                value=self._page if page else self._offset
            )
        return None

    def next_dict(self, page: bool = False) -> Optional[dict]:
        """
        Get's the next page configuration as dictionary.
        :param page: Specifies if the dictionary contains the page number or the offset.
         :type page: bool
        :return: A dictionary with the paginator's configuration for next page.
         :rtype: dict
        """
        if self._go_next():
            meta = {
                "count": self._count,
                "limit": self._limit
            }
            meta.update({"page": self._page} if page else {"offset": self._offset})
            return meta
        return None

    @staticmethod
    def _calculate_missing_data(count: int = 0, limit: int = 20, page: int = 1) -> (int, int):
        """
        Calculates missing data when reinitializing the paginator.
        :param count: Total number of resources.
         :type count: int
        :param limit: The limit used in pagination.
         :type limit: int
        :param page: The current page.
         :type page: int
        :return: A tuple of two integers representing the calculated offset and total number of pages.
         :rtype: (int, int)
        """
        result, rest = divmod(count, limit)
        return limit * (page - 1), result if not rest else result + 1

    def reinitialize(self, count: int = 0, limit: int = 20, page: int = 1) -> None:
        """
        Reinitializing the object's parameters.
        :param count: The total number of resources.
         :type count: int
        :param limit: The limit used in pagination.
         :type limit: int
        :param page: The current page.
         :type page: int
        """

        assert count > 0, "The count should be a positive number"
        assert limit > 0, "The limit should be a positive number"
        assert page > 0, "The page should be a positive number"

        offset, pages = self._calculate_missing_data(count, limit, page)

        assert page <= pages, "Page outside boundaries: {page} of {pages}".format(page=page, pages=pages)

        self._count = count
        self._limit = limit
        self._page = page
        self._offset = offset
        self._pages = pages
