from typing import Any, Callable


class Membership:
    def __init__(self, function: Callable[[Any], Any], items: list):
        self.function = function
        self.items = items

    def __call__(self, value: Any):
        return self.function(value)
