from typing import Any, Tuple

from ..base_var import VarSet
from ..inference_system import InferenceSystem
from ..predicates import Predicate
from ..rules import LarsenRule


class LarsenSystem(InferenceSystem):
    def __add__(self, other: Tuple[Any, ...]):
        try:
            antecedent, *consequences = other
        except ValueError:
            raise ValueError("The rule is not in the correct format")
        if not isinstance(antecedent, Predicate):
            raise ValueError("The antecedent is not Predicate")
        if any(map(lambda x: not isinstance(x, VarSet), consequences)):
            raise ValueError("The consequences is not a list of VarSet")
        rule = LarsenRule(antecedent, consequences)
        self.add_rule(rule)
        return self
