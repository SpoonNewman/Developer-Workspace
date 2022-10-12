from Controllers.Environment_controller.Event_Sequence_Manager.base_play_event import BasePlayEvent
from Controllers.Player_Registry_Actions import PlayerStandardActions


class EventsSecretShrineIntro(BasePlayEvent):
    def __init__(self) -> None:
        super().__init__()

        self.name = "Intro scene of investigating the hidden shrine"
        self.description = "You study the wall and notice a hidden switch on the wall"
        self.is_triggered = None # OnStudySecretRoom
        self.is_completed = None # OnStudyWallSwitchActivated
        self.possible_actions = self.get_possible_actions()
        self.next_scene = None

    def get_possible_actions(self):
        return [
            PlayerStandardActions.KILL_SELF,
            PlayerStandardActions.MOVE_FORWARD,
            PlayerStandardActions.MOVE_BACKWARD,
        ]
