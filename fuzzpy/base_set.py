from typing import Any, Callable

from numpy import arange

from .membership import Membership


class BaseSet:
    def __init__(
        self,
        name: str,
        membership: Membership,
        union: Callable[[Any, Any], Any],
        inter: Callable[[Any, Any], Any],
    ):
        self.name = name
        self.membership = membership
        self.union = union
        self.inter = inter

    def __and__(self, arg: "BaseSet"):
        memb = Membership(
            lambda x: self.union(
                self.membership(x),
                arg.membership(x),
            ),
            self.membership.items + arg.membership.items,
        )
        return BaseSet(
            f"({self.name})_union_({arg.name})",
            memb,
            union=self.union,
            inter=self.inter,
        )

    def __or__(self, arg: "BaseSet"):
        memb = Membership(
            lambda x: self.inter(
                self.membership(x),
                arg.membership(x),
            ),
            self.membership.items + arg.membership.items,
        )
        return BaseSet(
            f"({self.name})_inter_({arg.name})",
            memb,
            union=self.union,
            inter=self.inter,
        )

    def domain(self, step=0.05):
        start = self.membership.items[0]
        end = self.membership.items[-1]
        result = list(arange(start, end, step))
        result += self.membership.items
        result.sort()
        return result

    def __iter__(self):
        return iter(self.domain())

    def __len__(self):
        return len(self.domain())
