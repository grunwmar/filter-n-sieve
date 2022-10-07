import sys
from abc import ABC, abstractmethod
import re
from typing import Callable


# FILTER
class Filter(ABC):

    def __init__(self, **kwargs):
        self._kwargs = kwargs
        self._condition = None

    def __ror__(self, argument):

        if self._condition is None:
            return self.method(argument, **self._kwargs)
        else:
            if self._condition(argument):
                return self.method(argument, **self._kwargs)
            else:
                return argument

    def __getitem__(self, condition):
        self._condition = condition
        return self

    @abstractmethod
    def method(self): ...


# FILTER DECORATOR
def filter(func):
    class _Filter(Filter):
        def method(self, arg, **kwargs):
            return func(arg, **kwargs)

    return _Filter
