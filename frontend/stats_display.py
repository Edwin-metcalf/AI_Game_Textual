from textual.widgets import Static, Label
from textual.containers import Grid

class StatsDisplay(Static):
    def compose(self):
         Grid(
            Label("stats", classes="grid-labels"),
            Label(),
            Label("possible third grid for decision making or terminal thing", classes= "grid-labels"),
            classes="main-game-grid"
        )