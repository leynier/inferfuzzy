from typing import Any, List

from .base_set import BaseSet
from .base_var import VarSet
from .predicates import Predicate


class BaseRule:
    def __init__(self, antecedent: Predicate):
        self.antecedent = antecedent

    def __call__(self, values: dict):
        raise NotImplementedError()

    def __str__(self) -> str:
        return f"Antecedent: {self.antecedent}"


class Rule(BaseRule):
    def __init__(self, antecedent: Predicate, consequences: List[VarSet]):
        super(Rule, self).__init__(antecedent)
        self.consequences = consequences

    def aggregate(self, set: BaseSet, value: Any) -> BaseSet:
        raise NotImplementedError()

    def __call__(self, values: dict):
        value = self.antecedent(values)
        return {
            consequence.var.name: self.aggregate(
                consequence.set,
                value,
            )
            for consequence in self.consequences
        }

    def __str__(self) -> str:
        result = f"Antecedent: {self.antecedent}\n   "
        result += "Consequences:\n" + "\n".join(
            [f"      {x}" for x in self.consequences],
        )
        return result
