"""Provide the Base superclass."""
from abc import ABC, abstractmethod
from functools import partial


class Base(ABC):
    """Superclass for all models."""

    def __init__(self, client):
        """Initialize a Model instance.
        :param client: An instance of :class:`.Neuroscout`.
        """
        self._client = client

        all_methods = ('get', 'post', 'put', 'delete')
        assert set(self._auto_methods) <= set(all_methods)

        for method in self._auto_methods:
            setattr(self,
                    method,
                    partial(
                        getattr(self._client, "_" + method),
                        self._base_path)
                    )

    @property
    @abstractmethod
    def _base_path(self):
        pass

    @property
    @abstractmethod
    def _auto_methods(self):
        """ HTTP methods to auto create in subordinate classes """
        pass
