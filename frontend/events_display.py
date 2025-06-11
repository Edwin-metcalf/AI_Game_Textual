from textual.widgets import Static, Input,Label
from textual.containers import Vertical
from textual import on
from collections import deque

class EventsDisplay(Static):
    def __init__(self, game_manager):
        super().__init__()
        self.messages = deque()
        self.game_manager = game_manager
        

    def compose(self):
        yield Vertical(id="events-container")

    def on_mount(self):
        self.update_console()

    def update_console(self):
        container = self.query_one("#events-container",Vertical)
        container.remove_children()
        
        current_event = self.game_manager.get_current_event()

        if current_event:
            container.mount(Label(current_event.get_display_text(), classes="event-label"))
            self.input_widget = Input(placeholder="Enter your choice '1' or '2': ")
        else:
            if self.messages:
                for i in self.messages:
                    container.mount(Label(i, classes="event-label"))
            self.input_widget = Input(placeholder= "console")
        
        container.mount(self.input_widget)


    @on(Input.Submitted)
    def handle_input(self, event: Input.Submitted):
        user_input = event.value.strip()
        current_event = self.game_manager.get_current_event()
        if current_event:
            if self.game_manager.handle_event_response(user_input):
                self.messages.append(f"you chose {user_input} ")
                self.update_console()

                if hasattr(self, "parent_game") and self.parent_game:
                    self.parent_game.update_all_displays()
            else:
                self.messages.append("Invalid choice please try '1' or '2': ")
                self.update_console

        else:
            self.messages.append(f"> {user_input}")
            self.update_console
        event.input.value = ""



        
