from abc import abstractmethod
from Controllers.EventController import EventController
from Controllers.game_events import OnStaggeredMessageDisplayEvent, OnCurrentEventChange

class BaseSceneEvent():
    @classmethod
    def handle_event(cls):
        # TODO: Check for current scene and whether it matches this one.
        cls.display_description(description=cls.description)
        # cls.set_next_scene()

    @classmethod
    def set_next_scene(cls):
        event_change_evt = OnCurrentEventChange()
        event_change_evt.current_event = cls.next_scene
        EventController.broadcast_event(event_change_evt)

    @classmethod
    def display_description(cls, description: list[str] = None):
        evt = OnStaggeredMessageDisplayEvent()
        evt.messages = description
        EventController.broadcast_event(evt)