from .ai_backend import AiBackend
from .stats import Stats
from .nodes import PowerPlantNode


class GameManager():
    def __init__(self,version="0.1.1"):
        self.version = version
        self.stats = Stats()
        self.ai_backend = AiBackend(0)
        self.connected_nodes = []

    def power_plant_event(self):
        self.power_plant = PowerPlantNode(2,400)
        self.connected_nodes.append(self.power_plant)
        self.stats.connected_nodes.append(self.power_plant)
        
    
    def tick(self):
        self.stats.update_score()
        self.stats.update_energy()
        self.stats.update_money()
        self.stats.update_users()
        self.stats.get_stats_display()

        if self.stats.score == 3:
            self.power_plant_event()
        print(self.stats.score)
        
    



    
        