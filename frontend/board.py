from textual import on
from textual.widgets import Static, Button

class Board(Static):
    def __init__(self,game_manager, parent_game=None):
        super().__init__()
        self.game_manager = game_manager
        self.stats = self.game_manager.stats
        self.score = self.stats.score
        self.parent_game = parent_game

    def compose(self):
        yield Button(str(self.score), id = "ai-container")

    @on(Button.Pressed)
    def update_score(self):
        self.game_manager.tick()
        self.score = self.stats.score

        button = self.query_one("#ai-container", Button)
        button.label = str(self.score)

        if self.parent_game:
            self.parent_game.update_all_displays()
