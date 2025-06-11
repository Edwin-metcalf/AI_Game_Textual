from .ai_backend import AiBackend
from .stats import Stats
from .nodes import PowerPlantNode
from collections import deque
from .events import EVENT_REGISTRY


class GameManager():
    def __init__(self,version="0.1.1"):
        self.version = version
        self.stats = Stats()
        self.ai_backend = AiBackend(0)
        self.connected_nodes = []
        self.pending_events = deque()
        #self.events = Events()
        self.current_event = None
        self.triggered_events = set()



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

        self.check_events()
        print(f" this is the stats at GameManager Level: {self.stats.score}")
        

    def check_events(self):
        if self.stats.score in EVENT_REGISTRY and self.stats.score not in self.triggered_events:
            event_class = EVENT_REGISTRY[self.stats.score]
            event = event_class()
            self.pending_events.append(event)
            self.triggered_events.add(self.stats.score)

    def get_current_event(self):
        if not self.current_event and self.pending_events:
            self.current_event = self.pending_events.popleft()
        return self.current_event
    
    def handle_event_response(self, response):
        if self.current_event:
            try:
                choice = int(response.strip())
                if self.current_event.resolve(choice,self):
                    self.current_event = None
                    return True
                else:
                    return False
            except ValueError:
                return False
        return False
    



        
    



    
        