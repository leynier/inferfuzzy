from typing import Any, Callable, List, Union

from .base_set import BaseSet
from .predicates import Predicate


class VarSet(Predicate):
    def __init__(
        self,
        var: "BaseVar",
        set: BaseSet,
        union: Callable[[Any, Any], Any],
        inter: Callable[[Any, Any], Any],
    ):
        super(VarSet, self).__init__(union, inter)
        self.var = var
        self.set = set

    def __call__(self, values: dict):
        return self.set.membership(values[self.var.name])

    def __str__(self):
        return f"{self.var} in ({self.set})"


class BaseVar:
    def __init__(
        self,
        name: str,
        sets: List[BaseSet],
        union: Callable[[Any, Any], Any],
        inter: Callable[[Any, Any], Any],
    ):
        self.name = name
        self.sets = {set.name: set for set in sets}
        self.union = union
        self.inter = inter

    def into(self, set: Union[BaseSet, str]) -> VarSet:
        set_name = set.name if isinstance(set, BaseSet) else set
        if set_name not in self.sets:
            raise KeyError(f"Set {set_name} not found into var {self.name}")
        temp_set = self.sets[set_name]
        return VarSet(self, temp_set, self.union, self.inter)
