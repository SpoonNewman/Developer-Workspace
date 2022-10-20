from Controllers.Environment_controller.Event_Sequence_Manager.Events.base_story_event import BaseStoryEvent


class EventsGoblinAttackIntro(BaseStoryEvent):
    def __init__(self) -> None:
        super().__init__()

        self.name = ""
        self.description = "",
        self.is_triggered = None
        self.is_completed = None
        self.possible_actions = []
        self.next_scene = None # Can change throughout execution