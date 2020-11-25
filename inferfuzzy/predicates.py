from typing import Any, Callable


class Predicate:
    def __init__(
        self,
        union: Callable[[Any, Any], Any],
        inter: Callable[[Any, Any], Any],
    ) -> None:
        self.union = union
        self.inter = inter

    def __call__(self, values: dict):
        raise NotImplementedError()

    def __and__(self, other: "Predicate"):
        return AndPredicate(self, other, self.union, self.inter)

    def __or__(self, other: "Predicate"):
        return OrPredicate(self, other, self.union, self.inter)

    def __invert__(self):
        return NotPredicate(self, self.union, self.inter)


class BinaryPredicate(Predicate):
    def __init__(
        self,
        left: Predicate,
        right: Predicate,
        union: Callable[[Any, Any], Any],
        inter: Callable[[Any, Any], Any],
    ):
        super(BinaryPredicate, self).__init__(union, inter)
        self.left = left
        self.right = right


class AndPredicate(BinaryPredicate):
    def __call__(self, values: dict):
        return self.union(
            self.left(values),
            self.right(values),
        )

    def __str__(self):
        return f"({self.left} and {self.right})"


class OrPredicate(BinaryPredicate):
    def __call__(self, values: dict):
        return self.inter(
            self.left(values),
            self.right(values),
        )

    def __str__(self):
        return f"({self.left} or {self.right})"


class NotPredicate(Predicate):
    def __init__(
        self,
        arg: Predicate,
        union: Callable[[Any, Any], Any],
        inter: Callable[[Any, Any], Any],
    ):
        super(NotPredicate, self).__init__(union, inter)
        self.arg = arg

    def __call__(self, values: dict):
        return 1 - self.arg(values)

    def __str__(self):
        return f"(not {self.arg})"
