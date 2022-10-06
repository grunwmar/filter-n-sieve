```python
from filter import Filter, Sieve
...

```

```python
# Example of filter
class Colorize256(Filter):
    fg: int = 16
    bg: int = 255
    st: int = 0

    def method(self, value):
        return f"\033[{self.st};38;5;{self.fg}m\033[48;5;{self.bg}m{value}\033[0m"
        
```

```python
# Example of sieve
class MySieve(Sieve):
    negative: [lambda x: x < 0 ] = lambda x: abs(x)
    zero:     [lambda x: x == 0]
    positive: [lambda x: x > 0 ]

```

```python
nc = MySieve([-2,1,-5,-5,1,2,4,-0.5,0,0,1,6,7])
```
```
MySieve(negative=[2, 5, 5, 0.5], zero=[0, 0], positive=[1, 1, 2, 4, 1, 6, 7])
```
