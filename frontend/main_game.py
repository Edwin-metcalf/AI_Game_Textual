from textual.widgets import Footer, Header, Label, Static
from textual.containers import Grid
from .board import Board


class MainGame(Static):

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
            Label("stats", classes="grid-labels"),
            Board(),
            Label("possible third grid for decision making or terminal thing", classes= "grid-labels"),
            classes="main-game-grid"
        )