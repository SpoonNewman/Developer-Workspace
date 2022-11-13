from abc import abstractmethod
from typing import Dict
from Controllers.EventController import EventController

from Controllers.game_events import OnStaggeredMessageDisplayEvent, OnRecordPlayerAction, OnMessageDisplayEvent

class BaseSceneHandler():
    @classmethod
    @abstractmethod
    def handle_scene():
        raise NotImplementedError("This is using base class abstract property, please make your own!")

    @classmethod
    @abstractmethod
    def trigger_event():
        raise NotImplementedError("This is using base class abstract property, please make your own!")

    @classmethod
    def display_description(cls, description: list[str] = None):
        evt = OnStaggeredMessageDisplayEvent()
        evt.messages = description
        EventController.broadcast_event(evt)
 
    @classmethod
    def setup_scene_connections(cls, scene_connections = None, registered_scenes: Dict = {}):
        cls.registered_scenes=registered_scenes
        if scene_connections and len(scene_connections) > 0:
            cls.scene_connections = scene_connections

    @classmethod
    def record_action(cls, action, scene):
        evt = OnRecordPlayerAction()
        evt.action = action
        evt.scene = scene
        EventController.broadcast_event(evt)

    @classmethod
    def get_player_input(cls):
        evt = OnMessageDisplayEvent()
        evt.message = "\nWhat do you choose?  "
        evt.typewriter_display = 0
        EventController.broadcast_event(evt)