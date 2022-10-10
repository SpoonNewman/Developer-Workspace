from Controllers.Environment_controller import room_types

class EnvironmentController():
    def __init__(self) -> None:
        self.list_of_rooms = []

    def initialize_rooms(self) -> None:
        self.tunnel = room_types.room_tunnel(room_events=[], room_name="Intro Tunnel", room_exits=None)
        self.room_start = room_types.room(room_events=[], room_name="Fart Ass", room_exits=[self.tunnel])
        self.list_of_rooms = {
            "StartingArea": self.room_start
        }
        