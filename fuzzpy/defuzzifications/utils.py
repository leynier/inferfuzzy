from typing import Any, Callable

from ..base_set import BaseSet


def base_defuzzification(set: BaseSet, func: Callable[[Any, Any], bool]):
    best = -1
    best_value = 0
    for value in set:
        member_value = set.membership(value)
        if func(best, member_value):
            best_value = value
            best = member_value
    return best_value
