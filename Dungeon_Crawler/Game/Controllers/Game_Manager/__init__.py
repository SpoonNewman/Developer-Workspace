import sys
from Controllers.EventController import EventTypes, EventController
from Controllers.Messages_Controller import MessagesController
from Controllers.Player_Controller import PlayerController
from Controllers.Environment_controller import EnvironmentController
from Controllers.game_events import OnGameStartEvent, OnDieEvent, OnMessageDisplayEvent, OnStaggeredMessageDisplayEvent
from pygame import mixer

from constants import GameConstants

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
        EventController.add_listener(event_type=EventTypes.ON_GAME_START, handler_functions=[cls.initialize_music, cls.initialize_game_room_map, cls.begin_intro, cls.initialize_enemy_settings, PlayerController.initialize_player_settings])
        EventController.add_listener(event_type=EventTypes.ON_ITEM_PICKUP, handler_functions=[PlayerController.pickup_item])
        EventController.add_listener(event_type=EventTypes.ON_KILL_SELF, handler_functions=[cls.play_kill_self])
        EventController.add_listener(event_type=EventTypes.ON_DIE, handler_functions=[cls.play_dead_message, cls.kill_program])
        EventController.add_listener(event_type=EventTypes.ON_MESSAGE_DISPLAY, handler_functions=[MessagesController.display_message])
        EventController.add_listener(event_type=EventTypes.ON_STAGGERED_MESSAGE_DISPLAY, handler_functions=[MessagesController.display_staggered_messages])
        EventController.add_listener(event_type=EventTypes.ON_SHOW_AVAILABLE_ACTIONS, handler_functions=[MessagesController.show_available_actions])
        EventController.add_listener(event_type=EventTypes.ON_LOCATION_CHANGE, handler_functions=[PlayerController.set_current_location])

    @classmethod
    def initialize_music(cls, **kwargs):
        mixer.init()
        mixer.music.load(GameConstants.starting_music)
        mixer.music.set_volume(GameConstants.default_music_volume)
        mixer.music.play()
    
    @classmethod
    def start_game(cls):
        evt = OnGameStartEvent()
        EventController.broadcast_event(event_object=evt)

    @classmethod
    def begin_intro(cls, **kwargs):
        MessagesController.display_intro_message()

    @classmethod
    def initialize_game_room_map(cls, **kwargs):
        EnvironmentController.initialize_rooms()

    @classmethod
    def initialize_enemy_settings(cls, **kwargs):
        print("Initializing the enemy settings")

    @classmethod
    def play_dead_message(cls, **kwargs):
        evt = OnStaggeredMessageDisplayEvent()
        evt.messages = kwargs["event_object"].dead_message
        EventController.broadcast_event(event_object=evt)
        

    @classmethod
    def play_kill_self(cls, **kwargs):
        evt = OnMessageDisplayEvent()
        evt.message = kwargs["event_object"].kill_self_message
        EventController.broadcast_event(event_object=evt)

        dead_event = OnDieEvent()
        EventController.broadcast_event(event_object=dead_event)
   
    @classmethod
    def kill_program(cls, **kwargs):
        mixer.music.stop()
        sys.exit()
