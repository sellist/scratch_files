from itertools import product


def rolldice_sum_prob(sum_, dice_amount):
    """
    :param sum_: sum to calculate chance of
    :param dice_amount: amount of dice to use for calculating sum
    :return: chance of rolling sum with dice_amount in a non-converted float
    """
    dice_array = [list(range(1, 7)) for _ in range(dice_amount)]
    dice_perms = list(product(*dice_array))
    outcomes = [sum(x) for x in dice_perms]
    chance = outcomes.count(sum_)
    return chance / len(outcomes)
