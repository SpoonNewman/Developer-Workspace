class StartRoomSequence():
    def __init__(self) -> None:
        pass

    def handle_sequence(self):
        player_input = self.get_player_input()
        self.trigger_event_sequence()

    def get_player_input(self):
        return input("")

    def trigger_event_sequence(self):
        pass