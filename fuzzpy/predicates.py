from typing import Any, Callable

from .variable import Var


class Predicate:
    def __init__(
        self,
        norm: Callable[[Any, Any], Any],
        conorm: Callable[[Any, Any], Any],
    ) -> None:
        self.norm = norm
        self.conorm = conorm

    def __call__(self, values: dict):
        raise NotImplementedError()

    def __and__(self, other: "Predicate"):
        return AndPredicate(self, other, self.norm, self.conorm)

    def __or__(self, other: "Predicate"):
        return OrPredicate(self, other, self.norm, self.conorm)

    def __invert__(self):
        return NotPredicate(self, self.norm, self.conorm)


class BinaryPredicate(Predicate):
    def __init__(
        self,
        left: Predicate,
        right: Predicate,
        norm: Callable[[Any, Any], Any],
        conorm: Callable[[Any, Any], Any],
    ):
        super(BinaryPredicate, self).__init__(norm, conorm)
        self.left = left
        self.right = right


class AndPredicate(BinaryPredicate):
    def __call__(self, values: dict):
        return self.norm(
            self.left(values),
            self.right(values),
        )

    def __str__(self):
        return f"({self.left}) and ({self.right})"


class OrPredicate(BinaryPredicate):
    def __call__(self, values: dict):
        return self.conorm(
            self.left(values),
            self.right(values),
        )

    def __str__(self):
        return f"({self.left}) or ({self.right})"


class NotPredicate(Predicate):
    def __init__(
        self,
        arg: Predicate,
        norm: Callable[[Any, Any], Any],
        conorm: Callable[[Any, Any], Any],
    ):
        super(NotPredicate, self).__init__(norm, conorm)
        self.arg = arg

    def __call__(self, values: dict):
        return 1 - self.arg(values)

    def __str__(self):
        return f"not ({self.arg})"


class InPredicate(Predicate):
    def __init__(
        self,
        var: Var,
        desc: str,
        norm: Callable[[Any, Any], Any],
        conorm: Callable[[Any, Any], Any],
    ):
        super(InPredicate, self).__init__(norm, conorm)
        self.var = var
        self.desc = desc

    def __call__(self, values: dict):
        return self.var.get_membership(values[self.var.name], self.desc)

    def __str__(self):
        return f"{self.var} in ({self.desc})"


class InFactory:
    def __init__(
        self,
        norm: Callable[[Any, Any], Any],
        conorm: Callable[[Any, Any], Any],
    ):
        self.norm = norm
        self.conorm = conorm

    def __call__(self, var, desc: str) -> InPredicate:
        return InPredicate(var, desc, self.norm, self.conorm)

    @staticmethod
    def create(
        norm: Callable[[Any, Any], Any],
        conorm: Callable[[Any, Any], Any],
    ) -> "InFactory":
        return InFactory(norm, conorm)


In = InFactory.create(norm=min, conorm=max)
