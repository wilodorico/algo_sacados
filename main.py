import csv
from action import Action
from brute_force import glouton
from optimized import dynamic_programming_knapsack
from utils import DataUtils


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


if __name__ == "__main__":
    actions = read_csv_file("data/dataset_1.csv")
    # best_combination, max_benefit = glouton(actions, 500)

    # print(
    #     f"Meilleure combinaison d'actions: {[(action.name, action.cost, action.benefit_monnaie) for action in best_combination]}"
    # )
    # print(f"Bénéfice maximum: {max_benefit} euros")
    # print("cout total", sum([action.cost for action in best_combination]))
    # print("Total actions:", len(best_combination))

    # Tester dynamic_programming_knapsack
    best_combination2, max_benefit2 = dynamic_programming_knapsack(actions, 500)
    print(
        f"Meilleure combinaison (dynamic_programming_knapsack): {[(action.name, action.cost, action.benefit_monnaie) for action in best_combination2]}"
    )
    print(f"Bénéfice maximum (dynamic_programming_knapsack): {round(max_benefit2,2)} euros")

    print("cout total", sum([action.cost for action in best_combination2]))

    print("Total actions:", len(best_combination2))
