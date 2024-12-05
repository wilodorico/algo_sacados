from action import Action
from decorators import measure_memory, measure_time


@measure_time
@measure_memory
def dynamic_programming_knapsack(actions: list[Action], budget: float):
    # Convertir le budget en centimes pour éviter les erreurs d'arrondi
    budget = int(round(budget * 100))

    # Convertir les coûts et bénéfices des actions en centimes
    actions = [
        Action(
            action.name,
            int(round(action.cost * 100)),  # Coût en centimes
            action.benefit_percent,
            int(round(action.benefit_monnaie * 100)),  # Bénéfice en centimes
        )
        for action in actions
    ]

    actions_len = len(actions)

    # Créer une table (2D) pour stocker les meilleurs bénéfices
    dp = [[0] * (budget + 1) for _ in range(actions_len + 1)]

    # Remplir la table
    for i in range(1, actions_len + 1):
        for b in range(budget + 1):
            cost = actions[i - 1].cost
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
        cost = actions[i - 1].cost
        if dp[i][b] != dp[i - 1][b] and b >= cost:  # Vérification stricte du budget restant
            best_combination.append(actions[i - 1])
            b -= cost

    # Calculer le bénéfice total en euros
    max_benefit = dp[actions_len][budget] / 100

    # Reconvertir les coûts et bénéfices des actions en euros pour l'affichage
    best_combination = [
        Action(
            action.name,
            action.cost / 100,  # Coût en euros
            action.benefit_percent,
            action.benefit_monnaie / 100,  # Bénéfice en euros
        )
        for action in best_combination
    ]

    return best_combination, round(max_benefit, 2)
