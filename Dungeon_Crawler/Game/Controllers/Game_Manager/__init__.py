from cgitb import handler
import sys
from typing import Dict
from Controllers.EventController import EventTypes, EventController
from Controllers.Messages_Controller import MessagesController
from Controllers.Player_Controller import PlayerController, PlayerStandardActions
from Controllers.Environment_controller import EnvironmentController

# from events import Events

class GameManager():
    # __is_dead: bool = False
    # __current_location = None
    # valid_event_types = (EventTypes.ON_DIE.value, EventTypes.ON_MESSAGE_DISPLAY.value, EventTypes.ON_ROOM_MESSAGE_DISPLAY.value, EventTypes.ON_SHOW_AVAILABLE_ACTIONS.value, EventTypes.ON_PLAYER_INVESTIGATE.value, EventTypes.ON_KILL_SELF.value, EventTypes.ON_GAME_START.value, EventTypes.ON_PLAYER_ACTION.value, EventTypes.ON_ITEM_PICKUP.value)

    # # region Class Properties
    # @property
    # def is_dead(cls):
    #     return cls.__is_dead

    # @is_dead.setter    
    # def is_dead(cls, status: bool):
    #     cls.__is_dead = status
    #     if status:
    #         EventController.broadcast_event(EventTypes.ON_DIE)
    #         #  cls.__events.on_die()

    # @property
    # def current_location(cls):
    #     return cls.__current_location

    # @current_location.setter    
    # def current_location(cls, location):
    #     cls.__current_location = location
    #     if location:
    #         location.trigger_room_sequences()

    # endregion
    
    @classmethod
    def __init__(cls) -> None:
        cls.__events = None
        cls.initialize_event_subscriptions()
    
    @classmethod
    def initialize_event_subscriptions(cls):
        """Initialize the events and their subscriptions.
        """
        EventController.add_listener(event_type=EventTypes.ON_GAME_START, handler_functions=[cls.initialize_game_room_map, cls.begin_intro, cls.initialize_enemy_settings, PlayerController.initialize_player_settings])
        EventController.add_listener(event_type=EventTypes.ON_ITEM_PICKUP, handler_functions=[PlayerController.pickup_item])
        EventController.add_listener(event_type=EventTypes.ON_DIE, handler_functions=[cls.play_dead_message, cls.kill_program])
        EventController.add_listener(event_type=EventTypes.ON_MESSAGE_DISPLAY, handler_functions=[MessagesController.display_message])
        EventController.add_listener(event_type=EventTypes.ON_ROOM_MESSAGE_DISPLAY, handler_functions=[MessagesController.display_room_messages])
        EventController.add_listener(event_type=EventTypes.ON_SHOW_AVAILABLE_ACTIONS, handler_functions=[MessagesController.show_available_actions])

    @classmethod
    def initialize_game_room_map(cls):
        EnvironmentController.initialize_rooms()

    @classmethod
    def process_game_interval(cls):
        """Process an interval of actions within the game.
        """
        pass
    
    @classmethod
    def start_game(cls):
        EventController.broadcast_event(EventTypes.ON_GAME_START)

    @classmethod
    def begin_intro(cls):
        MessagesController.display_intro_message()

    @classmethod
    def initialize_enemy_settings(cls):
        print("Initializing the enemy settings")

    @classmethod
    def play_dead_message(cls):
        EventController.broadcast_event(EventTypes.ON_MESSAGE_DISPLAY, message="Game Over")
   
    @classmethod
    def kill_program(cls):
        sys.exit()
