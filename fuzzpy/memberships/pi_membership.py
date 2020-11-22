from ..membership import Membership


class PiMembership(Membership):
    def __init__(self, a, b, c, d):
        def func(x):
            if x <= a:
                return 0
            if a <= x and x <= b:
                return (x - a) / (b - a)
            if b <= x and x <= c:
                return 1
            if c <= x and x <= d:
                return (d - x) / (d - c)
            return 0

        super(PiMembership, self).__init__(func, [a, b, c, d])
