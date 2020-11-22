from fuzzpy.base_set import BaseSet
from typing import Any, Callable, Dict, List, Optional

from .rule import BaseRule


class InferenceSystem:
    def __init__(
        self,
        rules: Optional[List[BaseRule]] = None,
        defuzz_func: Optional[Callable[[BaseSet], Any]] = None,
    ):
        self.rules = rules if rules else []
        self.defuzz_func = defuzz_func

    def infer(
        self,
        values: dict,
        defuzz_func: Optional[Callable[[BaseSet], Any]] = None,
    ) -> Dict[str, Any]:
        if not self.rules:
            raise Exception("Empty rules")
        if self.defuzz_func is None and defuzz_func is None:
            raise Exception("Defuzzification not found")
        func = self.defuzz_func if defuzz_func is None else defuzz_func
        set: Dict[str, BaseSet] = self.rules[0](values)
        for rule in self.rules[1:]:
            update: Dict[str, BaseSet] = rule(values)
            for key in update:
                set[key] = set[key] & update[key]
        result: Dict[str, Any] = {}
        for key in set:
            result[key] = func(set[key])
        return result
