from ..base_set import BaseSet
from .utils import base_defuzzification


def lom_defuzzification(set: BaseSet):
    return base_defuzzification(set, lambda x, y: x <= y)
