from textual.widgets import Static, Button

class Board(Static):

    def compose(self):
        yield Button(id="ai-container")
    
