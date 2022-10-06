from filter import Filter, Sieve

# EXAMPLE OF FILTERS

class Colorize(Filter):
    fg: int = 0
    bg: int = 7
    st: int = 0

    def method(self, value):
        return f"\033[{self.st};3{self.fg};4{self.bg}m{value}\033[0m"


class Colorize256(Filter):
    fg: int = 16
    bg: int = 255
    st: int = 0

    def method(self, value):
        return f"\033[{self.st};38;5;{self.fg}m\033[48;5;{self.bg}m{value}\033[0m"


class RemoveTermColors(Filter):
    def method(self, value):
        find = re.compile(r'\u001B\[[0-9\;]+m')
        found = find.findall(value)
        for f in found:
            value = value.replace(f, "")
        return value


# EXAMPLE OF SIEVE

class MySieve(Sieve):
    negative: [lambda x: x < 0 ] = lambda x: abs(x)
    zero:     [lambda x: x == 0]
    positive: [lambda x: x > 0 ]

nc = MySieve([-2,1,-5,-5,1,2,4,-0.5,0,0,1,6,7])
#
# MySieve(negative=[2, 5, 5, 0.5], zero=[0, 0], positive=[1, 1, 2, 4, 1, 6, 7])
#
