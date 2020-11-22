from typing import Any, List

from .set import SetBase


class Var:
    def __init__(self, name: str, sets: List[SetBase]):
        self.name = name
        self.sets = {set.name: set for set in sets}

    def get_membership(self, value: Any, set_name: str):
        return self.sets[set_name].membership(value)
