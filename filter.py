import sys
from abc import ABC, abstractmethod
import re
from typing import Callable


# FILTER
class Filter(ABC):

    def __init__(self, **kwargs):
        tmp_dict = {}
        if hasattr(self.__class__, '__annotations__'):

            # checks if value of predefined attribute has is has correct type
            for attr, typ in self.__class__.__annotations__.items():
                value = self.__class__.__dict__.get(attr)
                if value is not None:
                    if not isinstance(value, typ):
                        raise TypeError(f"Value {value!r} of attribute {attr!r} is not type {self.__class__.__annotations__[attr]!r}")
                else:
                    tmp_dict.update({attr: None})

            tmp_dict.update({k: v for k, v in filter(lambda x: not x[0].startswith("_") and x[0]!="method", self.__class__.__dict__.items())})

            # checks if entered attribute is on list of allowed attributes
            # checks if entered attribute has correct type
            for attr, value in kwargs.items():
                if attr in tmp_dict:
                    if isinstance(value, self.__class__.__annotations__[attr]):
                        tmp_dict.update({attr: value})
                    else:
                        raise TypeError(f"Value {value!r} of attribute {attr!r} is not type {self.__class__.__annotations__[attr]!r}")
                else:
                    raise KeyError(f"Attribute {attr!r} is not defined")

            self.__dict__.update(tmp_dict)

    def __invert__(self):
        """Causes that the filter will just pass entered value as it is without any changes."""
        """Example of usage

                new_value = value | filter_1() | filter_2() | filter_3()

            but it is needed to turn off some filter due to a test, let say
            filter_2, so the tilde operator is applied before

                new_value = value | filter_1() | ~filter_2() | filter_3()

            is equivalent to

                new_value = value | filter_1() | filter_3()
        """
        self.method = lambda value: value
        return self


    def __ror__(self, value):
        """Applies itself to object before | after which the filter stands -> new_value = value | filter()."""
        """It allows the filters to be chained -> new_value = value | filter_1() | filter_2() | ... | filter_n()."""
        return self.method(value)

    @abstractmethod
    def method(self, value):
        """Proper filter method which has to be specified when deriving filter class."""
        ...


# SIEVE
class Sieve:
    """Divide a pack of values to some groups defined by condition."""

    def __init__(self, iterable):
        self._iterable = iterable
        for group, conditions in self.__annotations__.items():
            final_function = self.__class__.__dict__.get(group)
            tmp_list = []
            for condition in conditions:
                for i in self._iterable:
                    if condition(i):
                        if final_function is None:
                            tmp_list.append(i)
                        else:
                            if callable(final_function):
                                tmp_list.append(final_function(i))
                            else:
                                tmp_list.append(final_function)
            self.__dict__[group] = tmp_list


    def __len__(self):
        """Return number of groups."""
        return len(self.__dict__)-1


    def __str__(self):
        pairs = ", ".join([f"{a}={v!r}" for a, v in filter(lambda x: not x[0].startswith("_"), self.__dict__.items())])
        return f"{self.__class__.__name__}({pairs})"
