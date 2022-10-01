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


class room(base_room):
    def __init__(self) -> None:
        self.width = 0
        self.height = 0
        self.light = 0
        self.dampness = 0
        self.obstacles = 0
        self.shape = room_shape.OBLONG
        self.back = "back"
        self.exits = []
        super().get_events

    def trigger_events(self):
        return "Event is triggered"
        
    
    def get_events(self):
        return ["Some event from `room`"]

class room_tunnel(room):
    def __init__(self) -> None:
        super().__init__()

    def get_events(self):
        return ["Some event from `tunnel`"]

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