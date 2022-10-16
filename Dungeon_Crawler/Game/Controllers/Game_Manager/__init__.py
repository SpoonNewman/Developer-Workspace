from cgitb import handler
import sys
from typing import Dict
from Controllers.EventController import EventTypes, EventController
from Controllers.Messages_Controller import MessagesController
from Controllers.Player_Controller import PlayerController
from Controllers.Environment_controller import EnvironmentController
from Controllers.game_events import OnGameStartEvent

# from events import Events

class GameManager():
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
    def initialize_game_room_map(cls, **kwargs):
        EnvironmentController.initialize_rooms()

    @classmethod
    def process_game_interval(cls):
        """Process an interval of actions within the game.
        """
        pass
    
    @classmethod
    def start_game(cls):
        evt = OnGameStartEvent()
        EventController.broadcast_event(event_object=evt)

    @classmethod
    def begin_intro(cls, **kwargs):
        MessagesController.display_intro_message()

    @classmethod
    def initialize_enemy_settings(cls, **kwargs):
        print("Initializing the enemy settings")

    @classmethod
    def play_dead_message(cls, **kwargs):
        EventController.broadcast_event(EventTypes.ON_MESSAGE_DISPLAY, message="Game Over")
   
    @classmethod
    def kill_program(cls, **kwargs):
        sys.exit()
