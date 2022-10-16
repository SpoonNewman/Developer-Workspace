from . import room_types
import json

from Controllers.base_controller import BaseController

class EnvironmentController(BaseController):
    @classmethod
    def __init__(self) -> None:
        pass
    
    @classmethod
    def initialize_rooms(cls) -> None:
        """Initialize the room map with the correctly parsed depedency tree (sorted Breadth-First).

        Raises:
            ValueError: Raised when the searching for the room exit name in our collection of rooms is in error.
        """
        rooms_map = cls.get_rooms_from_config()
        
        # Order the rooms map by Breadth-First ordering
        ordered_rooms_map = cls.sort_dependency_tree(rooms_map)

        # Build all the rooms
        for room in ordered_rooms_map:
            cls.registered_rooms[room["name"]] = cls.build_room(room_config=room)

        for room in cls.registered_rooms.values():
            setattr(room, "registered_rooms", cls.registered_rooms)

        pass

    @classmethod
    def get_rooms_from_config(cls) -> dict:
        """Loads the configuration object from the json file.

        Returns:
            dict: The map of the room configuration.
        """
        with open("room_config.json") as config:
            return json.load(config)

    @classmethod
    def sort_dependency_tree (cls, rooms_map) -> dict:
        """Sorts and orders the depedency tree

        Args:
            rooms_map (Dict[str, Any]): The configuration dictionary object representing the map of the rooms

        Returns:
            Dict: The sorted room map.
        """
        temp_rooms_map = []
        # this currently only supports rooms with up to 4 possible exits
        # TODO: Would be cool to set the upper limit of this loop with the number
        # representing the highest number of dependencies in the collection of room objects
        for loop_pass in range(0, 5):
            temp_rooms_map += list(filter(lambda room: len(room["room_exits"]) == loop_pass, rooms_map))

        return temp_rooms_map

    @classmethod
    def build_room(cls, room_config):
        """Creates a room object based on a dictionary configuration object.

        Args:
            room_config (Dict[str, str | list[str] ]): The dictionary representing the desired configuration of rooms in the game.

        Raises:
            NotImplementedError: Raised when the `room type` does not match one of the supported values.

        Returns:
            Room: Returns a <Room> object or one of it's children
        """
        room_type = room_config["room_type"]
        if room_type == room_types.types.ROOM.value:
            return room_types.room(room_configuration=room_config)
        elif room_type == room_types.types.TUNNEL.value:
            return room_types.room_tunnel(room_configuration=room_config)
        elif room_type == room_types.types.TUNNEL_SPLIT.value:
            return room_types.room_tunnel_split(room_configuration=room_config)
        else:
            raise NotImplementedError("The room type that you passed in is not yet supported! Please create it or bug the devs")
