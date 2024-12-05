from action import Action
from decorators import measure_memory, measure_time


@measure_time
@measure_memory
def dynamic_programming_knapsack(actions: list[Action], budget: int):
    actions_len = len(actions)

    # Créer une table (2D) pour stocker les meilleurs bénéfices
    dp = [[0] * (budget + 1) for _ in range(actions_len + 1)]

    # Remplir la table
    for i in range(1, actions_len + 1):
        for b in range(budget + 1):
            cost = int(actions[i - 1].cost)
            if cost <= b:
                dp[i][b] = max(
                    dp[i - 1][b],  # Ne pas inclure l'action actuelle
                    dp[i - 1][b - cost] + actions[i - 1].benefit_monnaie,  # Inclure l'action
                )
            else:
                dp[i][b] = dp[i - 1][b]

    # Reconstituer les actions choisies
    best_combination = []
    b = budget
    for i in range(actions_len, 0, -1):
        if dp[i][b] != dp[i - 1][b]:  # Vérification si l'action a été incluse
            cost = int(actions[i - 1].cost)
            best_combination.append(actions[i - 1])
            b -= cost

    max_benefit = dp[actions_len][budget]
    return best_combination, round(max_benefit, 2)
