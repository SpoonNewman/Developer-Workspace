from Controllers.Environment_controller import room_types
import json

class EnvironmentController():
    def __init__(self) -> None:
        self.list_of_rooms = []

    # def initialize_rooms(self) -> None:
    #     self.tunnel = room_types.room_tunnel(room_events=[], room_name="Intro Tunnel", room_exits=None)
    #     self.room_start = room_types.room(room_events=[], room_name="Fart Ass", room_exits=[self.tunnel])
    #     self.list_of_rooms = {
    #         "StartingArea": self.room_start
    #     }
    
    def initialize_rooms(self) -> None:
        rooms_map = self.get_rooms_from_config()
        ordered_rooms_map = self.create_dependency_tree(rooms_map)
        for room in ordered_rooms_map:
            self.build_room(room_config=room)

    def get_rooms_from_config(self) -> dict:
        with open("room_config.json") as config:
            return json.load(config)

    def create_dependency_tree (self, rooms_map):
        temp_rooms_map = []
        # this currently only supports rooms with up to 4 possible exits
        for loop_pass in range(0, 5):
            temp_rooms_map += list(filter(lambda room: len(room["room_exits"]) == loop_pass, rooms_map))

        # TODO: create the rooted dependency tree, create the nodes
        # that don't have dependency in the `room_exits`
        # Would be a depth-first search where the levels are 
        # the number of dependencies the node has
        return temp_rooms_map

    def build_room(self, room_config):
        room_type = room_config["room_type"]
        if room_type == room_types.types.ROOM.value:
            return room_types.room(room_config)
        elif room_type == room_types.types.TUNNEL.value:
            return room_types.room_tunnel(room_config)
        elif room_type == room_types.types.TUNNEL_SPLIT.value:
            return room_types.room_tunnel_split(room_config)
        else:
            raise NotImplementedError("The room type that you passed in is not yet supported! Please create it or bug the devs")
