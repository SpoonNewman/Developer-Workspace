from cgitb import handler
import sys
import json
import pygame
from Controllers.EventController import EventTypes, EventController
from Controllers.Messages_Controller import MessagesController
from Controllers.Player_Controller import PlayerController
from Controllers.Environment_controller import EnvironmentController
from Controllers.game_events import OnGameStartEvent, OnDieEvent, OnMessageDisplayEvent, OnStaggeredMessageDisplayEvent
from Controllers.Music_Controller import MusicController, MusicSoundRegistry
from pygame import mixer
from Controllers.game_events import OnSfxPlayEvent
from Controllers.UI_Controller import UIManager, TextInput
from Controllers.game_events import OnGameInitializeEvent, OnCurrentEventChange
from Controllers.Surfaces_Registry import SurfacesRegistry
from constants import GameConstants

class GameManager():
    game_settings = {}
    is_new_game = True
    clock = pygame.time.Clock()
    fps = 60

    @classmethod
    def __init__(cls) -> None:
        cls.__events = None
        cls.load_settings()
        cls.initialize_event_subscriptions()

    @classmethod
    def load_settings(cls):
        with open("./game_settings_config.json") as config:
            cls.game_settings = json.load(config)
    
    @classmethod
    def initialize_event_subscriptions(cls):
        """Initialize the events and their subscriptions.
        """
        EventController.add_listener(event_type=EventTypes.ON_GAME_INITIALIZE, handler_functions=[cls.initialize_game_settings, cls.initialize_game_room_map, cls.initialize_enemy_settings, cls.initialize_player_settings])
        EventController.add_listener(event_type=EventTypes.ON_GAME_START, handler_functions=[cls.begin_game_loop])
        EventController.add_listener(event_type=EventTypes.ON_ITEM_PICKUP, handler_functions=[PlayerController.pickup_item])
        EventController.add_listener(event_type=EventTypes.ON_KILL_SELF, handler_functions=[cls.play_kill_self])
        EventController.add_listener(event_type=EventTypes.ON_DIE, handler_functions=[cls.play_dead_message, cls.kill_program])
        EventController.add_listener(event_type=EventTypes.ON_MESSAGE_DISPLAY, handler_functions=[MessagesController.display_message])
        EventController.add_listener(event_type=EventTypes.ON_STAGGERED_MESSAGE_DISPLAY, handler_functions=[MessagesController.display_staggered_messages])
        EventController.add_listener(event_type=EventTypes.ON_SHOW_AVAILABLE_ACTIONS, handler_functions=[MessagesController.show_available_actions])
        EventController.add_listener(event_type=EventTypes.ON_LOCATION_CHANGE, handler_functions=[PlayerController.set_current_location])
        EventController.add_listener(event_type=EventTypes.ON_MUSIC_TRACK_PLAY, handler_functions=[MusicController.play_music_by_track])
        EventController.add_listener(event_type=EventTypes.ON_SFX_PLAY, handler_functions=[MusicController.play_sfx])
        EventController.add_listener(event_type=EventTypes.ON_SFX_STOP, handler_functions=[MusicController.stop_sfx])
        EventController.add_listener(event_type=EventTypes.ON_VOLUME_CHANGE, handler_functions=[MusicController.change_volume])
        EventController.add_listener(event_type=EventTypes.ON_INVENTORY_DISPLAY, handler_functions=[PlayerController.display_inventory])
        EventController.add_listener(event_type=EventTypes.ON_SHOW_ITEM_ACTIONS, handler_functions=[MessagesController.show_item_actions])
        EventController.add_listener(event_type=EventTypes.ON_ITEM_DROP, handler_functions=[PlayerController.drop_from_inventory])
        EventController.add_listener(event_type=EventTypes.ON_NEXT_EVENT_CHANGE, handler_functions=[PlayerController.set_next_event])
        EventController.add_listener(event_type=EventTypes.ON_CURRENT_EVENT_CHANGE, handler_functions=[PlayerController.set_current_event])
        EventController.add_listener(event_type=EventTypes.ON_RECORD_PLAYER_ACTION, handler_functions=[PlayerController.record_action])
        EventController.add_listener(event_type=EventTypes.ON_PLAYER_STAT_CHANGE, handler_functions=[PlayerController.set_stat, UIManager.update_player_status])

    @classmethod
    def initialize_game_settings(cls, event):
        UIManager.initialize()
        cls.initialize_message_settings()
        MusicController.initialize_music(play_audio=cls.game_settings["play_audio"])

    @classmethod
    def initialize_player_settings(cls, event):
        PlayerController.initialize_player_settings(settings=cls.game_settings)

    @classmethod
    def initialize_message_settings(cls):
        MessagesController.default_typewriter_delay = GameConstants.typewriter_speeds[cls.game_settings["message_typewriter_speed"]].value
    
    @classmethod
    def start_game(cls):
        evt = OnGameInitializeEvent()
        EventController.broadcast_event(evt)

        cls.update_clock()

        start_evt = OnGameStartEvent()
        EventController.broadcast_event(start_evt)

    @classmethod
    def update_clock(cls):
        cls.clock.tick(cls.fps)

    @classmethod
    def begin_intro(cls):
        MessagesController.display_intro_message()

    @classmethod
    def initialize_game_room_map(cls, event):
        EnvironmentController.initialize_rooms()

    @classmethod
    def initialize_enemy_settings(cls, event):
        pass

    @classmethod
    def begin_game_loop(cls, event):
        while True:
            # if UIManager.main_menu.is_enabled():
            #     UIManager.main_menu.start_main_loop()
            pygame.event.pump()
            if cls.is_new_game:
                cls.begin_intro()
                cls.is_new_game = False
            
            current_location = PlayerController.get_current_location() # Check that player location is set
            
            if current_location:
                initial_scene_state = PlayerController.get_current_event()
                if initial_scene_state:
                    PlayerController.trigger_current_event(initial_scene_state)
                else:
                    current_location.trigger_description() # Trigger Sequence
                
                UIManager.clear_input_field() # Wipe the input box
                input_evt = OnMessageDisplayEvent()
                input_evt.message = "What do you do?  "
                input_evt.surface_key = SurfacesRegistry.PLAYER_INPUT_SURFACE
                EventController.broadcast_event(input_evt)

                player_input = TextInput.get_input()
                updated_scene_state = PlayerController.get_current_event()
                current_location.trigger_scene_event(player_input, updated_scene_state) # Perform actions/updates
            cls.update_clock()

    @classmethod
    def set_next_scene(cls, current_scene):
        next_evt = OnCurrentEventChange()
        next_evt.current_event = current_scene.next_scene
        EventController.broadcast_event(next_evt)

    @classmethod
    def play_dead_message(cls, event):
        dead_sound = OnSfxPlayEvent()
        dead_sound.sfx_name = MusicSoundRegistry.PLAYER_DEATH_CRY
        EventController.broadcast_event(dead_sound)
        
        evt = OnStaggeredMessageDisplayEvent()
        evt.messages = event.dead_message
        EventController.broadcast_event(evt)

        

    @classmethod
    def play_kill_self(cls, event):
        evt = OnMessageDisplayEvent()
        evt.message = event.kill_self_message
        EventController.broadcast_event(evt)

        dead_event = OnDieEvent()
        EventController.broadcast_event(dead_event)
   
    @classmethod
    def kill_program(cls, event):
        mixer.music.stop()
        sys.exit()
