from itertools import combinations
from decorators import measure_memory, measure_time
from action import Action


@measure_time
@measure_memory
def glouton(actions: list[Action], budget: int):
    actions_sort = sorted(actions, key=lambda x: x.benefit_monnaie, reverse=True)

    best_combination = []
    max_benefit = 0

    for action in actions_sort:
        if action.cost <= budget:
            best_combination.append(action)
            budget -= action.cost
            max_benefit = max_benefit + action.benefit_monnaie

    return best_combination, round(max_benefit, 2)


@measure_time
@measure_memory
def brute_force(actions: list[Action], budget: int):
    best_combination = []
    max_benefit = 0

    # Tester toutes les combinaisons possibles
    for subset_size in range(1, len(actions) + 1):
        for subset in combinations(actions, subset_size):
            cost = sum([action.cost for action in subset])
            benefit = sum([action.benefit_monnaie for action in subset])
            if cost <= budget and benefit > max_benefit:
                best_combination = subset
                max_benefit = benefit

    return best_combination, max_benefit
