from Controllers.Environment_controller import room_types
import json

class EnvironmentController():
    def __init__(self) -> None:
        self.list_of_rooms = []
    
    def initialize_rooms(self) -> None:
        """Initialize the room map with the correctly parsed depedency tree (sorted Breadth-First).

        Raises:
            ValueError: Raised when the searching for the room exit name in our collection of rooms is in error.
        """
        rooms_map = self.get_rooms_from_config()
        
        # Order the rooms map by Breadth-First ordering
        ordered_rooms_map = self.sort_dependency_tree(rooms_map)

        # Build all the rooms
        for room in ordered_rooms_map:
            self.list_of_rooms.append(self.build_room(room_config=room))

        # Loop over the rooms we've built
        for room in self.list_of_rooms:
            if len(room.room_exits) > 0:
                # Loop over the exits of the room
                for exit_name in room.room_exits:
                    # Grab the room object from the name, i.e. room_exit
                    dependant_rooms = list(filter(lambda dependant_room: exit_name == dependant_room.room_name, self.list_of_rooms))
                    if len(dependant_rooms) != 1:
                        raise ValueError("Either the dependant room wasn't registered or there are duplicates.")

                    # Should only be one element in dependant_rooms
                    # Look in our room_exits -> then replace the room_name in our exits with the id instead
                    for dependant_room in dependant_rooms:
                        room.room_exits = list(map(lambda exit: exit.replace(dependant_room.room_name, dependant_room._id), room.room_exits))

                    # Result: Each room dependency, which is our room_exits, now contain UUIDs instead of names to refer to the room
                    # This enables strong identification whereas a name is fairly weak.

            # TODO: Parse and replace the event names with the actual event objects.

    def get_rooms_from_config(self) -> dict:
        """Loads the configuration object from the json file.

        Returns:
            dict: The map of the room configuration.
        """
        with open("room_config.json") as config:
            return json.load(config)

    def sort_dependency_tree (self, rooms_map) -> dict:
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

    def build_room(self, room_config):
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
