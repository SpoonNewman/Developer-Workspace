from enum import Enum
from abc import ABC, abstractmethod

class room_shape(Enum):
    ROUND = "round"
    RECTANGULAR = "rectangular"
    OBLONG = "oblong"


class base_room(ABC):
    @abstractmethod
    def get_events(self):
        pass

    @abstractmethod
    def trigger_events():
        pass
        # We need to pop an event off when the event is triggered
    
    
    @abstractmethod
    def on_frequently_visited(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def room_name(self):
        raise NotImplementedError       
   
    @property
    @abstractmethod
    def room_events(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def room_entrance(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def room_exits(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def player_visits_to_room(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def width(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def height(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def light(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def dampness(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def obstacles(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def shape(self):
        raise NotImplementedError


class room(base_room):
    def __init__(self, room_entrance=None, room_events=[], room_name="Fart ass room", room_exits=[]) -> None:
        self.width = 0
        self.height = 0
        self.light = 0
        self.dampness = 0
        self.obstacles = 0
        self.shape = room_shape.OBLONG
        self.room_exits = room_exits
        self.room_name = room_name
        self.room_events = room_events
        self.room_entrance = room_entrance
        super().get_events

    def trigger_events(self):
        return "Event is triggered"
        
    
    def get_events(self):
        return self.room_events

class room_tunnel(room):
    def __init__(self, room_entrance=None, room_events=[], room_name="Fart ass room") -> None:
        super().__init__(room_entrance=room_entrance, room_events=room_events, room_name=room_name)


class room_intersection(room):
    def __init__(self) -> None:
        super().__init__()

        self.left = "left"
        self.right = "right"
        self.forward = "forward"
    pass

class room_dead_end(room):
    def __init__(self) -> None:
        super().__init__()
    pass

class room_tunnel_split(room):
    def __init__(self) -> None:
        super().__init__()
        self.left = "left"
        self.right = "right"
    pass

class room_secret(room_dead_end):
    def __init__(self) -> None:
        super().__init__()
        self.secret = "secret"
    pass

someRoom = room_tunnel()
print(someRoom.get_events())