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
