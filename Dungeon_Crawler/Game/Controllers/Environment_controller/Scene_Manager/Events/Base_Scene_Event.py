from abc import abstractmethod
from Controllers.EventController import EventController
from Controllers.game_events import OnStaggeredMessageDisplayEvent

class BaseSceneEvent():
    @classmethod
    @abstractmethod
    def handle_event(cls):
        raise NotImplementedError("This is using base class abstract property, please make your own!")

    @classmethod
    @abstractmethod
    def trigger_next_scene(cls):
        raise NotImplementedError("This is using base class abstract property, please make your own!")

    @classmethod
    def display_description(cls, description: list[str] = None):
        evt = OnStaggeredMessageDisplayEvent()
        evt.messages = description
        EventController.broadcast_event(evt)