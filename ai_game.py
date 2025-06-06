from textual.app import App
from textual.widgets import Label
from frontend.main_game import MainGame
from backend.game_manager import GameManager

class AiGame(App):
    CSS_PATH = "frontend/grid_columns.tcss"

    def __init__(self):
        super().__init__()
        self.game_manager = GameManager()

    def compose(self):
        yield Label("hello world")
        yield MainGame(game_manager = self.game_manager, id="MainGame")

if __name__ == "__main__":
    AiGame().run()