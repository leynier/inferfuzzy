from typing import Any, Callable

from numpy import arange

from .membership import Membership


class BaseSet:
    def __init__(
        self,
        name: str,
        membership: Membership,
        aggregation: Callable[[Any, Any], Any],
    ):
        self.name = name
        self.membership = membership
        self.aggregation = aggregation

    def __add__(self, arg: "BaseSet"):
        memb = Membership(
            lambda x: self.aggregation(
                self.membership(x),
                arg.membership(x),
            ),
            self.membership.items + arg.membership.items,
        )
        return BaseSet(
            f"({self.name})_union_({arg.name})",
            memb,
            aggregation=self.aggregation,
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
