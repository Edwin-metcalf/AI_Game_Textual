from textual.widgets import Static, Input,Label
from textual.containers import Vertical
from textual import on

class EventsDisplay(Static):
    def __init__(self):
        super().__init__()
        self.messages = []
    def compose(self):
        yield Vertical(id="events-container")

    def on_mount(self):
        self.update_console()
    
    def update_console(self):
        container = self.query_one("#events-container",Vertical)
        container.remove_children()


        if self.messages:
            for i in self.messages:
                container.mount(Label(i, "event-label"))
        
        container.mount(Input(placeholder="console"))



        
