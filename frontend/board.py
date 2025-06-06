from textual import on
from textual.widgets import Static, Button
from backend.game_manager import GameManager

class Board(Static):
    def __init__(self):
        super().__init__()
        self.backend = GameManager().ai_backend
        self.score = 0

    def compose(self):
        yield Button(str(self.score), id = "ai-container")

    @on(Button.Pressed)
    def update_score(self):
        self.score = self.backend.tick()

        button = self.query_one("#ai-container", Button)
        button.label = str(self.score)
