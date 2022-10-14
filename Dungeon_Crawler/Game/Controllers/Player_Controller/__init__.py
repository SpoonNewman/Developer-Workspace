from Controllers.base_controller import BaseController
from Controllers.Player_Registry_Actions import PlayerStandardActions
from Controllers.EventController import EventController, EventTypes
from Controllers.Environment_controller import EnvironmentController




class PlayerController():
    __is_dead: bool = False
    __current_location = None

    # region Class Properties
    @property
    def is_dead(self):
        return self.__is_dead

    @is_dead.setter    
    def is_dead(self, status: bool):
        self.__is_dead = status
        if status:
            EventController.broadcast_event(EventTypes.ON_DIE)
            #  cls.__events.on_die()

    @property
    def current_location(self):
        return self.__current_location

    @current_location.setter    
    def current_location(self, location):
        self.__current_location = location
        if location:
            location.trigger_room_sequences()

    @classmethod
    def __init__(cls) -> None:
        pass

    @classmethod
    def initialize_player_settings(cls):
        print("Setting up the player settings")
        cls.current_location = EnvironmentController.registered_rooms["start_room"]
        pass


    @classmethod
    def get_available_actions(cls, room):  
        pass

    @classmethod
    def get_player_input(cls, action_type: str):
        pass
    
    @classmethod
    def actions_by_room_type(cls, room_type: str):
        return []

    @classmethod
    def pickup_item(cls):
        pass
        

