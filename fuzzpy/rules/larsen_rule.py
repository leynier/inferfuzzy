from typing import Any

from ..base_set import BaseSet
from ..membership import Membership
from ..rule import Rule


class LarsenRule(Rule):
    def aggregate(self, set: BaseSet, value: Any) -> BaseSet:
        membership = Membership(
            lambda x: set.membership(x) * value,
            set.membership.items,
        )
        return BaseSet(f"scaled_{set.name}", membership, set.aggregation)
