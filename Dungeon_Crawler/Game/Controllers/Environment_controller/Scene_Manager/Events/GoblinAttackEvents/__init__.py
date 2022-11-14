from Controllers.Environment_controller.Scene_Manager.Events.Base_Scene_Event import BaseSceneEvent


class EventsGoblinAttackIntro(BaseSceneEvent):
    def __init__(self) -> None:
        super().__init__()

        self.name = ""
        self.description = "",
        self.is_triggered = None
        self.is_completed = None
        self.possible_actions = []
        self.next_scene = None # Can change throughout execution