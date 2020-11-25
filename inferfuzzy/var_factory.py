from typing import Any, Callable, List, Optional

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

    def __call__(
        self,
        name: str,
        sets: Optional[List[BaseSet]] = None,
    ) -> BaseVar:
        return BaseVar(name, self.union, self.inter, sets)

    @staticmethod
    def create(
        union: Callable[[Any, Any], Any],
        inter: Callable[[Any, Any], Any],
    ) -> "VarFactory":
        return VarFactory(union, inter)
