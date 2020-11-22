from ..base_set import BaseSet


def bisection_defuzzification(set: BaseSet):
    sums = []
    for value in set:
        try:
            sums.append(set.membership(value) + sums[-1])
        except IndexError:
            sums.append(set.membership(value))
    values = list(set)
    for index in range(len(values)):
        if sums[index] >= sums[-1] / 2:
            return values[index]
