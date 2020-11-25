from ..membership import Membership


class GammaMembership(Membership):
    def __init__(self, a, m):
        def func(x):
            if x <= a:
                return 0
            if a <= x and x <= m:
                return (x - a) / (m - a)
            return 1

        super(GammaMembership, self).__init__(func, [a, m])
