from textual.widgets import Static, Label
from textual.containers import Vertical

class StatsDisplay(Static):
    def __init__(self,backend_stats):
        super().__init__()
        self.stats = backend_stats

         
    def compose(self):
        yield Vertical(id="stats-container")

    def on_mount(self):
        self.update_stats()
    

    def update_stats(self):
        container = self.query_one("#stats-container", Vertical)
        container.remove_children()

        stat_list = self.stats.get_stats_display()
        for i in stat_list:
            container.mount(Label(i, classes="stat-label"))
