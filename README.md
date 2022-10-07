
```python
from filter import filter, Filter


```
# by decorator
```python
""" Example of decorator use """
@filter
def color256(string, fg=83, bg=129, sty=0):
    return f"\033[{sty};38;5;{fg}m\033[48;5;{bg}m{string}\033[0m"


strings_case_1 = [
        "Hello!" | color256(sty=1),
        "Hello!" | color256(sty=1) [lambda x: x == "Hello!"],
        "hello"  | color256(sty=1) [lambda x: x == "Hello!"],
    ]

print("\n* by decorator:", *strings_case_1)
```


# by abstract class
```python
""" Example of abstract class use """
class Color(Filter):
    def method(self, string, fg=129, bg=83, sty=0):
        return f"\033[{sty};38;5;{fg}m\033[48;5;{bg}m{string}\033[0m"

strings_case_2 = [
        "Hello!" | Color(sty=1),
        "Hello!" | Color(sty=1) [lambda x: x == "Hello!"],
        "Hello"  | Color(sty=1) [lambda x: x == "Hello!"],
    ]

print("\n* by abs class:", *strings_case_2)
```
