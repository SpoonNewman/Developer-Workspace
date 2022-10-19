from Controllers.base_controller import BaseController
from Controllers.Player_Registry_Actions import PlayerStandardActions
from Controllers.EventController import EventController, EventTypes




class PlayerController(BaseController):
    __is_dead: bool = False
    __current_location = None

    # region Class Properties
    @property
    def get_is_dead(cls):
        return cls.__is_dead

    @classmethod
    def set_is_dead(cls, status: bool):
        cls.__is_dead = status
        if status:
            EventController.broadcast_event(EventTypes.ON_DIE)

    @classmethod
    def get_current_location(cls):
        return cls.__current_location

    @classmethod
    def set_current_location(cls, location):
        cls.__current_location = location
        if location:
            location.trigger_room_sequences()

    @classmethod
    def __init__(cls) -> None:
        pass

    @classmethod
    def initialize_player_settings(cls, **kwargs):
        print("Setting up the player settings")
        cls.set_current_location(location=cls.registered_rooms["start_room"])

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
    def pickup_item(cls, **kwargs):
        pass
        
