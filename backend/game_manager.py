from .ai_backend import AiBackend
from .stats import Stats

class GameManager():
    def __init__(self,version="0.1.1"):
        self.version = version
        self.stats = Stats()
        self.ai_backend = AiBackend(0)

    
    def tick(self):
        self.stats.update_score()
        self.stats.update_energy()
        self.stats.update_money()
        self.stats.update_users()
        self.stats.get_stats_display()

    
        