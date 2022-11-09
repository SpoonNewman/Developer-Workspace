from enum import Enum
from abc import ABC, abstractmethod
from typing import Dict
from uuid import uuid4
from Controllers.Environment_controller.Scene_Manager.scene_handler_registry import SceneHandlerRegistry

class SceneTypes(Enum):
    STANDARD = 0

class BaseScene(ABC):
    registered_scenes = []

        # We need to pop an event off when the event is triggered
    @abstractmethod
    def trigger_description(self):
        raise NotImplementedError("This is using base class abstract property, please make your own!")

    @abstractmethod
    def trigger_scene_event(self):
        raise NotImplementedError("This is using base class abstract property, please make your own!")

class standard_scene(BaseScene):
    def __init__(self, scene_configuration: Dict) -> None:
        """Create a basic scene object.

        Args:
            Needs documented 
        """
        if not scene_configuration:
            raise ValueError("No configuration was passed to the room object.")
        self._id = str(uuid4())
        # self.width = 0
        # self.height = 0
        # self.light = 0
        # self.dampness = 0
        # self.obstacles = 0
        # self.shape = room_shape.OBLONG
        self.scene_connections = scene_configuration.get("scene_connections")
        self.scene_name = scene_configuration.get("name")
        self.scene_handler = scene_configuration.get("event_handler")

        if self.scene_handler:
            self.scene_handler = SceneHandlerRegistry.registry[self.scene_handler]
            
    def initialize_connections(self):
        if self.scene_handler:
            self.scene_handler.setup_scene_connections(scene_connections=self.scene_connections, registered_scenes=self.registered_scenes)
    
    def trigger_description(self):
        if self.scene_handler:
            self.scene_handler.display_description()

    def get_scene_events(self):
        if self.scene_handler:
            return self.scene_handler.scene_events

    
    def trigger_scene_event(self, input, current_scene_event = None):
        if self.scene_handler:
            self.scene_handler.trigger_event(input, current_scene_event)
