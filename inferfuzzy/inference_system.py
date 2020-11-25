from typing import Any, Callable, Dict, List, Optional

from .base_set import BaseSet
from .rule import BaseRule


class InferenceSystem:
    def __init__(
        self,
        rules: Optional[List[BaseRule]] = None,
        defuzz_func: Optional[Callable[[BaseSet], Any]] = None,
    ):
        self.rules = rules if rules else []
        self.defuzz_func = defuzz_func

    def add_rule(self, rule: BaseRule):
        self.rules.append(rule)

    def infer_with_custom_defuzz(
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
            temp: Dict[str, BaseSet] = rule(values)
            for key in temp:
                set[key] += temp[key]
        result: Dict[str, Any] = {}
        for key in set:
            result[key] = func(set[key])
        return result

    def infer_with_dict(
        self,
        values: dict,
    ) -> Dict[str, Any]:
        return self.infer_with_custom_defuzz(values)

    def infer(
        self,
        **values: dict,
    ) -> Dict[str, Any]:
        return self.infer_with_custom_defuzz(values)

    def __str__(self) -> str:
        result = f"Defuzzification function:\n   {self.defuzz_func.__name__}\n"
        result += "Rules:\n" + "\n".join([f"   {rule}" for rule in self.rules])
        return result
