

class Node:
    def __init__(self, score_bonus):
        self.bonus = score_bonus

class PowerPlantNode(Node):
    def __init__(self, score_bonus, energy_produced):
        super().__init__(score_bonus)

        self.bonus = score_bonus + 1
        self.energy_produced = energy_produced