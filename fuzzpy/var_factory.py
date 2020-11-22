from typing import Any, Callable, List

from .base_set import BaseSet
from .base_var import BaseVar


class VarFactory:
    def __init__(
        self,
        union: Callable[[Any, Any], Any],
        inter: Callable[[Any, Any], Any],
    ):
        self.union = union
        self.inter = inter

    def __call__(self, name: str, sets: List[BaseSet]) -> BaseVar:
        return BaseVar(name, sets, self.union, self.inter)

    @staticmethod
    def create(
        union: Callable[[Any, Any], Any],
        inter: Callable[[Any, Any], Any],
    ) -> "VarFactory":
        return VarFactory(union, inter)
