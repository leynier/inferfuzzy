from ..base_set import BaseSet


def centroid_defuzzification(set: BaseSet):
    numerator = 0
    denominator = 0
    for value in set:
        numerator += value * set.membership(value)
        denominator += set.membership(value)
    return numerator / denominator
