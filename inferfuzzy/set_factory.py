from typing import Any, Callable

from .base_set import BaseSet
from .membership import Membership


class SetFactory:
    def __init__(
        self,
        aggregation: Callable[[Any, Any], Any],
    ):
        self.aggregation = aggregation

    def __call__(
        self,
        name: str,
        membership: Membership,
    ) -> BaseSet:
        return BaseSet(name, membership, self.aggregation)

    @staticmethod
    def create(
        aggregation: Callable[[Any, Any], Any],
    ) -> "SetFactory":
        return SetFactory(aggregation)
