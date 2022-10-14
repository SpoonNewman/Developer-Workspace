from enum import Enum
from abc import ABC, abstractmethod
from typing import Dict
from uuid import uuid4

from Controllers.Environment_controller.Event_Sequence_Manager.story_events_registry import StoryEventsRegistry
from Controllers.Environment_controller.Event_Sequence_Manager.story_sequences_registry import StorySequencesRegistry

# TODO: Add auto creation of UUID for ID property

class room_shape(Enum):
    ROUND = "round"
    RECTANGULAR = "rectangular"
    OBLONG = "oblong"

class types(Enum):
    ROOM = "room"
    TUNNEL = "tunnel"
    TUNNEL_SPLIT = "tunnel_split"

# class base_room(ABC):
        # We need to pop an event off when the event is triggered
    
    #region
    # @abstractmethod
    # def on_frequently_visited(self):
    #     raise NotImplementedError

    # @property
    # @abstractmethod
    # def room_name(self):
    #     raise NotImplementedError       
   
    # @property
    # @abstractmethod
    # def room_events(self):
    #     raise NotImplementedError

    # @property
    # @abstractmethod
    # def room_entrance(self):
    #     raise NotImplementedError

    # @property
    # @abstractmethod
    # def room_exits(self):
    #     raise NotImplementedError

    # @property
    # @abstractmethod
    # def player_visits_to_room(self):
    #     raise NotImplementedError

    # @property
    # @abstractmethod
    # def width(self):
    #     raise NotImplementedError

    # @property
    # @abstractmethod
    # def height(self):
    #     raise NotImplementedError

    # @property
    # @abstractmethod
    # def light(self):
    #     raise NotImplementedError

    # @property
    # @abstractmethod
    # def dampness(self):
    #     raise NotImplementedError

    # @property
    # @abstractmethod
    # def obstacles(self):
    #     raise NotImplementedError

    # @property
    # @abstractmethod
    # def shape(self):
    #     raise NotImplementedError
    #endregion


class room():
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
            self.event_handler = StorySequencesRegistry().registry[tmp_event_handler_key]
    
    def trigger_room_sequences(self):
        self.event_handler.handle_sequence()

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
        pass
    
    def get_events(self):
        pass


class room_intersection(room):
    def __init__(self, room_configuration: Dict) -> None:
        """Create an Intersection object.

        Args:
            room_exits (list[str]): The list of room names that represent exits from the current room. Defaults to "None"  
            room_name (str): The name of the room you are creating. Defaults to "None"  
            room_events (list[RoomEvent]): A list of room events that should be triggered by player action. Defaults to "None"  
        """
        super().__init__(room_configuration)

class room_dead_end(room):
    def __init__(self) -> None:
        super().__init__()

class room_tunnel_split(room):
    def __init__(self, room_configuration: Dict) -> None:
        super().__init__(room_configuration=room_configuration)

    def trigger_room_sequences(self):
        pass
    
    def get_events(self):
        pass

class room_secret(room_dead_end):
    def __init__(self) -> None:
        super().__init__()
