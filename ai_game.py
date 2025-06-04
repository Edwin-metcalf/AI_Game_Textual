from textual.app import App
from textual.widgets import Label
from frontend.main_game import MainGame

class AiGame(App):
    CSS_PATH = "frontend/grid_columns.tcss"

    def compose(self):
        yield Label("hello world")
        yield MainGame(id="MainGame")

if __name__ == "__main__":
    AiGame().run()