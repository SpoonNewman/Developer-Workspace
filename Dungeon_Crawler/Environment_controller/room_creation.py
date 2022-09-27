from enum import Enum
from tkinter import ROUND
from turtle import right, shape, width

class room_shape(Enum):
    ROUND = "round"
    RECTANGULAR = "rectangular"
    OBLONG = "oblong"

class base_room():
    width = 0
    height = 0
    light = 0
    dampness = 0
    obstacles = 0
    shape = room_shape.OBLONG
    back = "back"
    exits = []
    pass

class room_tunnel(base_room):
    pass

class room_intersection(base_room):
    left = "left"
    right = "right"
    forward = "forward"
    pass

class room_dead_end(base_room):
    pass

class room_tunnel_split(base_room):
    left = "left"
    right = "right"
    pass

class room_secret(room_dead_end):
    secret = "secret"
    pass

