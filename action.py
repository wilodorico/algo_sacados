from dataclasses import dataclass


@dataclass
class Action:
    name: str
    cost: float
    benefit_percent: float
    benefit_monnaie: float = None

    def __post_init__(self):
        self.benefit_monnaie = self.calcul_benefit_monnaie()

    def calcul_benefit_monnaie(self) -> float:
        benefit = self.cost * self.benefit_percent / 100
        return round(benefit, 2)
