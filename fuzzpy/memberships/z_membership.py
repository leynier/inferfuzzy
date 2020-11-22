from ..membership import Membership


class ZMembership(Membership):
    def __init__(self, a, c):
        def func(x):
            if x <= a:
                return 1
            if a < x and x <= (a + c) / 2:
                return 1 - 2 * ((x - a) / (c - a)) ** 2
            if (a + c) / 2 < x and x < c:
                return 2 * ((c - x) / (c - a)) ** 2
            return 0

        super(ZMembership, self).__init__(func, [a, (a + c) / 2, c])
