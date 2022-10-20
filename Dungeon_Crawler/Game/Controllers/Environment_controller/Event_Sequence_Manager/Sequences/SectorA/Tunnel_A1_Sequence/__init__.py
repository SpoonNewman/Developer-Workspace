from Game.Controllers.Environment_controller.Event_Sequence_Manager.Sequences.Base_Sequence import BaseSequence


class TunnelA1Sequence(BaseSequence):
    def __init__(self) -> None:
        pass

    def handle_sequence(self):
        player_input = self.get_player_input()
        # if player_input == "some action"
        #   self.trigger_sequence()
        # elif player_input == "some other action"
        #   self.trigger_sequence()

    def trigger_sequence(self):
        pass