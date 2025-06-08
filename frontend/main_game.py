from textual.widgets import Footer, Header, Label, Static
from textual.containers import Grid
from .board import Board
from .stats_display import StatsDisplay
from .events_display import EventsDisplay


class MainGame(Static):
    def __init__(self, game_manager, **kwargs):
        super().__init__(**kwargs)
        self.game_manager = game_manager
        self.stats_display = StatsDisplay(self.game_manager.stats)
        self.board = Board(self.game_manager, parent_game = self)
        self.events_display = EventsDisplay()

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
            self.events_display,
            classes="main-game-grid"
        )
    
    def update_all_displays(self):
        self.stats_display.update_stats()