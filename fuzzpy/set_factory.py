from typing import Any, Callable

from .base_set import BaseSet
from .membership import Membership


class SetFactory:
    def __init__(
        self,
        union: Callable[[Any, Any], Any],
        inter: Callable[[Any, Any], Any],
    ):
        self.union = union
        self.inter = inter

    def __call__(
        self,
        name: str,
        membership: Membership,
    ) -> BaseSet:
        return BaseSet(name, membership, self.union, self.inter)

    @staticmethod
    def create(
        union: Callable[[Any, Any], Any],
        inter: Callable[[Any, Any], Any],
    ) -> "SetFactory":
        return SetFactory(union, inter)
