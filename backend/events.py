

class Event:
    def __init__(self,message, options):
        self.message = message
        self.options = options 
        self.resolved = False

    def get_display_text(self):
        text = f"{self.message}\n"
        for i, (options,_) in enumerate(self.options, 1):
            text += f"{i}: {options}"
        return text
    
    def resolve(self, choice_number, game_manager):
        if 1 <= choice_number <= len(self.options):
            _ , option_value = self.options[choice_number - 1]
            self.handle_choice(game_manager, option_value)
            self.resolve = True
        return False
    def handle_choice(self, game_manager, choice):
        pass #will be overided in childern classes
        
class WebScrapeEvent(Event):
    def __init__(self):
        super().__init__(
            message="Your AI needs more data! How are you going to get more data?", 
            options= [
                ("Scrape the internet (free but at what cost)", "scrape"),
                ("Purchase data (Expensive but you know what your getting)", "purchase")])
    
    def handle_choice(self, game_manager, choice):
        if choice == "scrape":
            game_manager.stats.score += 10
        elif choice == "purchase":
            game_manager.stats.score +=10
            game_manager.stats.money_total -=300

EVENT_REGISTRY = {
    5: WebScrapeEvent
}
        





