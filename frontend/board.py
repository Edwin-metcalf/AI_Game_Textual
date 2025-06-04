from textual import on
from textual.widgets import Static, Button
from backend.ai_backend import AiBackend

class Board(Static):
    def __init__(self):
        super().__init__()
        self.backend = AiBackend()
        self.score = 0

    def compose(self):
        yield Button(str(self.score), id = "ai-container")

    @on(Button.Pressed)
    def update_score(self):
        self.score = self.backend.tick()

        button = self.query_one("#ai-container", Button)
        button.label = str(self.score)
