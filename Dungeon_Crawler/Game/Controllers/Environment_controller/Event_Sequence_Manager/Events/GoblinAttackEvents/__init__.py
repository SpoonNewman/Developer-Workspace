from Controllers.Environment_controller.Event_Sequence_Manager.base_play_event import BasePlayEvent


class EventsGoblinAttackIntro(BasePlayEvent):
    def __init__(self) -> None:
        super().__init__()

        self.name = ""
        self.description = "",
        self.is_triggered = None
        self.is_completed = None
        self.possible_actions = []
        self.next_scene = None # Can change throughout execution