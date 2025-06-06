
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

    def update_score(self):
        self.score += self.current_score_tick
        return self.score


    def update_users(self):
        self.users = int(self.score * 10)
    
    def update_money(self):
        self.money_produced = round(self.score * 2.3, 2)
        self.money_total += round(self.money_produced - self.costs, 2)

    def update_energy(self, connected_nodes):
        self.costs = 0
        if self.energy_total < 0:
            self.energy_total = 0
        self.energy_consumed += self.score * 5

        #for i in connected_nodes find nodes and do stuff with power

    def get_stats_display(self):
        return [
            f"VERSION: {self.version}",
            f"USERS: {self.users}",
            f"MONEY: TOTAL ${self.money_total:.2f} MADE: ${self.money_produced:.2f} COSTS: ${self.costs:.2f} ",
            f"ENERGY: USED: {self.energy_used} kWh, PRODUCED: {self.energy_produced} kWh, TOTAL: {self.energy_total} kWh"
        ]    
        

