from ..base_set import BaseSet
from .lom_defuzzification import lom_defuzzification
from .som_defuzzification import som_defuzzification


def mom_defuzzification(set: BaseSet):
    min_max = som_defuzzification(set)
    max_max = lom_defuzzification(set)
    return (min_max + max_max) / 2
