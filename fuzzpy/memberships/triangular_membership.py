from ..membership import Membership


class TriangularMembership(Membership):
    def __init__(self, a, m, b):
        def func(x):
            if x <= a:
                return 0
            if a <= x and x <= m:
                return (x - a) / (m - a)
            if m <= x and x <= b:
                return (b - x) / (b - m)
            return 0

        super(TriangularMembership, self).__init__(func, [a, m, b])
