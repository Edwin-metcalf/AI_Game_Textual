from .stats import Stats

class AiBackend:
    def __init__(self, version="0.1.1"):
        
        self.stats = Stats(version)
        self.score = 0

    def tick(self):
        self.score += self.stats.update_score()
        return self.score


