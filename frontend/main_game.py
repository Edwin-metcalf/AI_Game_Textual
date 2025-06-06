from textual.widgets import Footer, Header, Label, Static
from textual.containers import Grid
from .board import Board
from .stats_display import StatsDisplay


class MainGame(Static):
    def __init__(self, game_manager, **kwargs):
        super().__init__(**kwargs)
        self.game_manager = game_manager
        self.stats_display = StatsDisplay()
        self.board = Board()

    def compose(self):
        yield self.header()
        yield self.grid()
        yield self.footer()
        
    def header(self):
        return Header()
        
    def footer(self):
        return Footer()

    def grid(self):
        return Grid(
            self.stats_display,
            self.board,
            Label("possible third grid for decision making or terminal thing", classes= "grid-labels"),
            classes="main-game-grid"
        )