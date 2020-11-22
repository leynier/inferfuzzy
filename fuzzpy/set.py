from typing import Any, Callable

from .membership import Membership


class SetBase:
    def __init__(
        self,
        name: str,
        membership: Membership,
        norm: Callable[[Any, Any], Any],
        conorm: Callable[[Any, Any], Any],
    ):
        self.name = name
        self.membership = membership
        self.norm = norm
        self.conorm = conorm

    def __add__(self, arg: "SetBase"):
        memb = Membership(
            lambda x: self.norm(
                self.membership(x),
                arg.membership(x),
            ),
            self.membership.items + arg.membership.items,
        )
        return SetBase(
            f"({self.name})_union_({arg.name})",
            memb,
            norm=self.norm,
            conorm=self.conorm,
        )

    def __mul__(self, arg: "SetBase"):
        memb = Membership(
            lambda x: self.conorm(
                self.membership(x),
                arg.membership(x),
            ),
            self.membership.items + arg.membership.items,
        )
        return SetBase(
            f"({self.name})_inter_({arg.name})",
            memb,
            norm=self.norm,
            conorm=self.conorm,
        )


class SetFactory:
    def __init__(
        self,
        norm: Callable[[Any, Any], Any],
        conorm: Callable[[Any, Any], Any],
    ):
        self.norm = norm
        self.conorm = conorm

    def __call__(
        self,
        name: str,
        membership: Membership,
    ) -> SetBase:
        return SetBase(name, membership, self.norm, self.conorm)

    @staticmethod
    def create(
        norm: Callable[[Any, Any], Any],
        conorm: Callable[[Any, Any], Any],
    ) -> "SetFactory":
        return SetFactory(norm, conorm)


Set = SetFactory.create(norm=min, conorm=max)
