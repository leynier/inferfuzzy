from .predicates import Predicate


class Rule:
    def __init__(self, antecedent: Predicate):
        self.antecedent = antecedent

    def __call__(self, values: dict):
        raise NotImplementedError()
