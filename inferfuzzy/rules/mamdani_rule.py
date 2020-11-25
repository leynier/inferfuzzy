from typing import Any

from ..base_set import BaseSet
from ..membership import Membership
from ..rule import Rule


class MamdaniRule(Rule):
    def aggregate(self, set: BaseSet, value: Any) -> BaseSet:
        membership = Membership(
            lambda x: min(value, set.membership(x)),
            set.membership.items,
        )
        return BaseSet(f"cuted_{set.name}", membership, set.aggregation)
