from abc import abstractmethod
from Controllers.Environment_controller.Event_Sequence_Manager.Sequences.Base_Story import BaseStory

class BaseStoryEvent(BaseStory):
    @classmethod
    @abstractmethod
    def handle_event(cls):
        raise NotImplementedError("This is using base class abstract property, please make your own!")

    @classmethod
    @abstractmethod
    def trigger_next_scene(cls):
        raise NotImplementedError("This is using base class abstract property, please make your own!")
