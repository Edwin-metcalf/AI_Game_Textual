from .nodes import PowerPlantNode

class Stats:
    def __init__(self,version="0.1.1"):
        self.users = 0
        self.version = version

        self.energy_total = 0
        self.energy_produced = 0
        self.energy_consumed = 0

        self.money_total = 0.00
        self.money_produced = 0.00
        self.costs = 0.00

        self.score = 0
        self.current_score_tick = 1

        self.connected_nodes = []

    def update_score(self):
        self.score += self.current_score_tick
        return self.score


    def update_users(self):
        self.users = int(self.score * 10)
    
    def update_money(self):
        self.money_produced = round(self.score * 2.3, 2)
        self.money_total += round(self.money_produced - self.costs, 2)

    def update_energy(self):
        self.costs = 0
        if self.energy_total < 0:
            self.energy_total = 0
        self.energy_consumed += self.score * 5

        for i in self.connected_nodes:
            if isinstance(i, PowerPlantNode):
                self.energy_produced += i.energy_produced

        self.energy_total += self.energy_produced - self.energy_consumed

        if self.energy_total < 0:
            energy_cost = round(abs(self.energy_total) // 7.4, 2)
            self.costs += round(energy_cost, 2)
            print(f"You used {self.energy_total} more then you produced and had to pay ${energy_cost}")

    def get_stats_display(self):
        return [
            f"VERSION: {self.version}\n",
            f"USERS: {self.users}\n",
            f"MONEY: \nTOTAL ${self.money_total:.2f} \nMADE: ${self.money_produced:.2f} \nCOSTS: ${self.costs:.2f}\n",
            f"ENERGY: \nUSED: {self.energy_produced} kWh, \nPRODUCED: {self.energy_produced} kWh, \nTOTAL: {self.energy_total} kWh\n"
        ]    
        

