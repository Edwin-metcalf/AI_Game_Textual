
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

        #self.score = 0 I think this will be handled in ai_backend 
        self.current_score_tick = 1

    def update_score(self):
        #just return the amount the ai goes up and its added to total in ai_backend
        return self.current_score_tick

