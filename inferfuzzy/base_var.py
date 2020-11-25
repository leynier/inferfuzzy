from typing import Any, Callable, List, Optional, Tuple, Union, cast

import matplotlib.pyplot as plt

from .base_set import BaseSet
from .membership import Membership
from .predicates import Predicate
from .set import Set


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
        return f"({self.var} in {self.set})"


class BaseVar:
    def __init__(
        self,
        name: str,
        union: Callable[[Any, Any], Any],
        inter: Callable[[Any, Any], Any],
        sets: Optional[List[BaseSet]] = None,
    ):
        self.name = name
        self.sets = {set.name: set for set in sets} if sets else {}
        self.union = union
        self.inter = inter

    def into(self, set: Union[BaseSet, str]) -> VarSet:
        set_name = set.name if isinstance(set, BaseSet) else set
        if set_name not in self.sets:
            raise KeyError(f"Set {set_name} not found into var {self.name}")
        temp_set = self.sets[set_name]
        return VarSet(self, temp_set, self.union, self.inter)

    def __add__(
        self,
        arg: Union[
            Tuple[str, Membership],
            BaseSet,
            Tuple[BaseSet, ...],
        ],
    ):
        temp: List[BaseSet] = []
        if (
            isinstance(arg, tuple)
            and len(arg) == 2
            and isinstance(arg[0], str)
            and isinstance(arg[1], Membership)
        ):
            name = cast(str, arg[0])
            membership = cast(Membership, arg[1])
            temp.append(Set(name=name, membership=membership))
        elif isinstance(arg, BaseSet):
            temp.append(arg)
        elif isinstance(arg, tuple) and all(
            map(lambda x: isinstance(x, BaseSet), arg),
        ):
            temp += arg
        else:
            raise ValueError("Incorrect format of set")
        self.sets.update({set.name: set for set in temp})
        return self

    def graph(self, step: float = 0.05):
        plots = []
        plt.figure()
        for it, desc in enumerate(self.sets.values()):
            x_data = desc.domain(step=step)
            y_data = [desc.membership(x) for x in x_data]
            plots.append(plt.plot(x_data, y_data, f"C{it+1}", label=desc.name))
        plt.legend()
        plt.title(self.name)
        plt.savefig(f"var_{self.name}.png")

    def __str__(self) -> str:
        return self.name
