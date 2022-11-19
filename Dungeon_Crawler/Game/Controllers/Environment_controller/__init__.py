from .scene_types import SceneTypes, standard_scene
import json

from Controllers.base_controller import BaseController

class EnvironmentController(BaseController):
    @classmethod
    def __init__(self) -> None:
        pass
    
    @classmethod
    def initialize_scenes(cls) -> None:
        """Initialize the scene map with the correctly parsed depedency tree (sorted Breadth-First).

        Raises:
            ValueError: Raised when the searching for the room exit name in our collection of rooms is in error.
        """
        scenes_map = cls.get_scenes_from_config()
        
        # Order the rooms map by Breadth-First ordering
        ordered_scenes_map = cls.sort_dependency_tree(scenes_map)

        # Build all the scenes
        for scene in ordered_scenes_map:
            cls.registered_scenes[scene["name"]] = cls.build_scene(scene_config=scene)

        for scene in cls.registered_scenes.values():
            scene.registered_scenes = cls.registered_scenes

    @classmethod
    def get_scenes_from_config(cls) -> dict:
        """Loads the configuration object from the json file.

        Returns:
            dict: The map of the scene configuration.
        """
        with open("scene_config.json") as config:
            return json.load(config)

    @classmethod
    def sort_dependency_tree (cls, scenes_map) -> dict:
        """Sorts and orders the depedency tree by number of scene connections.

        Args:
            scenes_map (Dict[str, Any]): The configuration dictionary object representing the map of the scenes

        Returns:
            Dict: The sorted scene map.
        """
        upper_limit_scene_connections = 0
        for scene in scenes_map:
            upper_limit_scene_connections = len(scene["scene_connections"]) if len(scene["scene_connections"]) > upper_limit_scene_connections else upper_limit_scene_connections

        temp_scenes_map = []
        for loop_pass in range(0, upper_limit_scene_connections+1):
            temp_scenes_map += list(filter(lambda scene: len(scene["scene_connections"]) == loop_pass, scenes_map))

        return temp_scenes_map

    @classmethod
    def build_scene(cls, scene_config):
        """Creates a scene object based on a dictionary configuration object.

        Args:
            scene_config (Dict[str, str | list[str] ]): The dictionary representing the desired configuration of rooms in the game.

        Raises:
            NotImplementedError: Raised when the `scene type` does not match one of the supported values.

        Returns:
            Room: Returns a <Room> object or one of it's children
        """
        scene_type = scene_config["scene_type"]
        if scene_type == SceneTypes.STANDARD.name.lower():
            return standard_scene(scene_configuration=scene_config)
        else:
            raise NotImplementedError("The scene type that you passed in is not yet supported! Please create it or bug the devs")
