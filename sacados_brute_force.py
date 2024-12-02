import csv
import logging
from itertools import combinations

from decorators import measure_memory, measure_time
from action import Action


# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


class DataUtils:
    @staticmethod
    def convert_to_float(value: str) -> float:
        try:
            return round(float(value), 2)
        except ValueError as e:
            logging.error(f"Erreur de conversion pour la valeur '{value}': {e}")
            raise ValueError(f"La valeur '{value}' n'est pas un nombre valide.")

    @staticmethod
    def retrieve_percent_from_string(value: str):
        return value.replace("%", "")


class InvestmentStrategy:

    @staticmethod
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

        return best_combination, max_benefit

    @staticmethod
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


def read_csv_file(file_path):
    """Lit un fichier CSV et retourne une liste des actions.

    Args:
        file_path (str): Chemin du fichier CSV.

    Returns:
        actions (list[dict]): Liste des actions avec leur nom, coût et bénéfice.
    """
    with open(file_path, "r", encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Ignorer la première ligne
        actions = []
        for row in csv_reader:
            name = row[0]
            try:
                cost: float = DataUtils.convert_to_float(row[1])
                benefit_percent: str = DataUtils.retrieve_percent_from_string(row[2])
                benefit_percent: float = DataUtils.convert_to_float(benefit_percent)

                if cost > 0 and benefit_percent > 0:
                    action = Action(name, cost, benefit_percent)
                    actions.append(action)
            except ValueError as e:
                print(f"Erreur de conversion pour la ligne: {row}: {e}")
                continue  # Passer à la ligne suivante

    return actions


data = read_csv_file("data/dataset_1.csv")

best_combination, max_benefit = InvestmentStrategy.glouton(data, 500)

print(
    f"Meilleure combinaison d'actions: {[(action.name, action.cost, action.benefit_monnaie) for action in best_combination]}"
)
print(f"Bénéfice maximum: {max_benefit} euros")
print("cout total", sum([action.cost for action in best_combination]))
print("Total actions:", len(best_combination))


# Tester dynamic_programming_knapsack
best_combination2, max_benefit2 = InvestmentStrategy.dynamic_programming_knapsack(data, 500)
print(
    f"Meilleure combinaison (dynamic_programming_knapsack): {[(action.name, action.cost, action.benefit_monnaie) for action in best_combination]}"
)
print(f"Bénéfice maximum (dynamic_programming_knapsack): {round(max_benefit2,2)} euros")

print("cout total", sum([action.cost for action in best_combination2]))

print("Total actions:", len(best_combination2))
