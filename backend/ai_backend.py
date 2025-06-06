

class AiBackend:
    def __init__(self,score=0, version="0.1.1"):
        self.score = score

    def tick(self,score):
        self.score = score
        return self.score


