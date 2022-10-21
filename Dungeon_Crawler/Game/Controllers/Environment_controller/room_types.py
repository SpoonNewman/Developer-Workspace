from enum import Enum
from abc import ABC, abstractmethod
from typing import Dict
from uuid import uuid4
from Controllers.Environment_controller.Event_Sequence_Manager.story_sequences_registry import StorySequencesRegistry

class room_shape(Enum):
    ROUND = "round"
    RECTANGULAR = "rectangular"
    OBLONG = "oblong"

class types(Enum):
    ROOM = "room"
    TUNNEL = "tunnel"
    CHAMBER = "chamber"
class BaseRoom(ABC):
        # We need to pop an event off when the event is triggered
    @abstractmethod
    def trigger_room_sequences(self):
        raise NotImplementedError("This is using base class abstract property, please make your own!")

class room(BaseRoom):
    def __init__(self, room_configuration: Dict) -> None:
        """Create a basic room object.

        Args:
            room_exits (list[str]): The list of room names that represent exits from the current room. Defaults to "None"  
            room_name (str): The name of the room you are creating. Defaults to "None"  
            room_events (list[RoomEvent]): A list of room events that should be triggered by player action. Defaults to "None"  
        """
        if not room_configuration:
            raise ValueError("No configuration was passed to the room object.")
        self._id = str(uuid4())
        self.width = 0
        self.height = 0
        self.light = 0
        self.dampness = 0
        self.obstacles = 0
        self.shape = room_shape.OBLONG
        self.room_exits = room_configuration.get("room_exits")
        self.room_name = room_configuration.get("name")
        self.event_handler = room_configuration.get("event_handler")

        if self.event_handler:
            tmp_event_handler_key = self.event_handler
            self.event_handler = StorySequencesRegistry.registry[tmp_event_handler_key]
    
    def trigger_room_sequences(self):
        self.event_handler.handle_sequence(room_exits=self.room_exits, registered_rooms=self.registered_rooms)

class room_tunnel(room):
    """Create a Tunnel object.

        Args:
            room_exits (list[str]): The list of room names that represent exits from the current room. Defaults to "None"  
            room_name (str): The name of the room you are creating. Defaults to "None"  
            room_events (list[RoomEvent]): A list of room events that should be triggered by player action. Defaults to "None"  
        """
    def __init__(self, room_configuration: Dict) -> None:
        super().__init__(room_configuration=room_configuration)

    def trigger_room_sequences(self):
        self.event_handler.handle_sequence(room_exits=self.room_exits, registered_rooms=self.registered_rooms)


class room_intersection(room):
    def __init__(self, room_configuration: Dict) -> None:
        """Create an Intersection object.

        Args:
            room_exits (list[str]): The list of room names that represent exits from the current room. Defaults to "None"  
            room_name (str): The name of the room you are creating. Defaults to "None"  
            room_events (list[RoomEvent]): A list of room events that should be triggered by player action. Defaults to "None"  
        """
        super().__init__(room_configuration)

    def trigger_room_sequences(self):
        pass

class room_dead_end():
    def __init__(self) -> None:
        super().__init__()

    def trigger_room_sequences(self):
        pass

class room_secret(room_dead_end):
    def __init__(self) -> None:
        super().__init__()

    def trigger_room_sequences(self):
        pass

class chamber(room):
    def __init__(self, room_configuration: Dict) -> None:
        super().__init__(room_configuration)

    # def trigger_room_sequences(self):
    #     pass