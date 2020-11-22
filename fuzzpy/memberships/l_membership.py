from ..membership import Membership


class LMembership(Membership):
    def __init__(self, a, m):
        def func(x):
            if x <= a:
                return 1
            if a <= x and x <= m:
                return (m - x) / (m - a)
            return 0

        super(LMembership, self).__init__(func, [a, m])
