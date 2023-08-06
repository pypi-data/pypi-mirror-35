"""Contains base classes for models and related classes."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from saltant.exceptions import BadHttpRequestError


class Model(object):
    """Base class for representing a model."""
    def __str__(self):
        """String representation of model."""
        raise NotImplementedError


class ModelManager(object):
    """Base class for a model manager.

    Attributes:
        _client (:py:class:`saltant.client.Client`): An authenticated
            saltant client.
        list_url (str): The URL to list models.
        detail_url (str): The URL format to get specific models.
        model (:py:class:`saltant.models.resource.Model`): The model
            being used.
    """
    list_url = "NotImplemented"
    detail_url = "NotImplemented"
    model = Model

    def __init__(self, _client):
        """Save the client so we can make API calls in the manager.

        Args:
            _client (:py:class:`saltant.client.Client`): An
                authenticated saltant client.
        """
        self._client = _client

    def list(self):
        """List instances of models."""
        raise NotImplementedError

    def get(self):
        """Get a specific instance of a model."""
        raise NotImplementedError

    def create(self):
        """Create an instance of a model."""
        raise NotImplementedError

    @classmethod
    def response_data_to_model_instance(cls, response_data):
        """Convert response data to a model.

        Args:
            response_data (dict): The data from the request's response.
        """
        raise NotImplementedError

    @staticmethod
    def validate_request_success(
            response_text,
            request_url,
            status_code,
            expected_status_code,):
        """Validates that a request was successful.

        Args:
            response_text (str): The response body of the request.
            request_url (str): The URL the request was made at.
            status_code (int): The status code of the response.
            expected_status_code (int): The expected status code of the
                response.

        Raises:
            :py:class:`saltant.exceptions.BadHttpRequestError`: The HTTP
                request failed.
        """
        try:
            assert status_code == expected_status_code
        except AssertionError:
            msg = ("Request to {url} failed with status {status_code}:\n"
                   "The reponse from the request was as follows:\n\n"
                   "{content}").format(
                       url=request_url,
                       status_code=status_code,
                       content=response_text,)
            raise BadHttpRequestError(msg)
