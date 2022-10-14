from cgitb import handler
import sys
from typing import Dict
from Controllers.EventController import EventTypes, EventController
from Controllers.Messages_Controller import MessagesController
from Controllers.Player_Controller import PlayerController, PlayerStandardActions
from Controllers.Environment_controller import EnvironmentController

# from events import Events

def initialize_game_controllers():
    return MessagesController(), PlayerController(), EnvironmentController()

class GameManager():
    __is_dead: bool = False
    __current_location = None
    # valid_event_types = (EventTypes.ON_DIE.value, EventTypes.ON_MESSAGE_DISPLAY.value, EventTypes.ON_ROOM_MESSAGE_DISPLAY.value, EventTypes.ON_SHOW_AVAILABLE_ACTIONS.value, EventTypes.ON_PLAYER_INVESTIGATE.value, EventTypes.ON_KILL_SELF.value, EventTypes.ON_GAME_START.value, EventTypes.ON_PLAYER_ACTION.value, EventTypes.ON_ITEM_PICKUP.value)

    @property
    def is_dead(self):
        return self.__is_dead

    @is_dead.setter    
    def is_dead(self, status: bool):
        self.__is_dead = status
        if status:
            EventController.broadcast_event(EventTypes.ON_DIE)
            #  self.__events.on_die()

    @property
    def current_location(self):
        return self.__current_location

    @current_location.setter    
    def current_location(self, location):
        self.__current_location = location
        if location:
            location.trigger_room_sequences()

    
    def __init__(self) -> None:
        # self.__events = Events((self.valid_event_types))
        self.__events = None
        self.messages_controller, self.player_controller, self.environment_controller = initialize_game_controllers()
        self.initialize_event_subscriptions()
    
    def process_game_interval(self):
        """Process an interval of actions within the game.
        """
        # current_actions = self.messages_controller.show_available_actions(game_manager.player_controller, None)
        # self.current_location.get_available_actions()
        current_action_input = input("Make your selection:  ") # Show Prompt of things they can do
        # self.player_take_action(current_actions[current_action_input])
    
    def initialize_game_room_map(self):
        self.environment_controller.initialize_rooms()
        self.current_location = self.environment_controller.registered_rooms["start_room"]

    def initialize_event_subscriptions(self):
        """Initialize the events and their subscriptions.
        """
        EventController.add_listener(event_type=EventTypes.ON_GAME_START, handler_functions=[self.initialize_game_room_map, self.begin_intro, self.initialize_player_settings, self.initialize_enemy_settings])
        EventController.add_listener(event_type=EventTypes.ON_ITEM_PICKUP, handler_functions=[self.pickup_item])
        EventController.add_listener(event_type=EventTypes.ON_DIE, handler_functions=[self.play_dead_message, self.kill_program])
        EventController.add_listener(event_type=EventTypes.ON_MESSAGE_DISPLAY, handler_functions=[self.messages_controller.display_message])
        EventController.add_listener(event_type=EventTypes.ON_ROOM_MESSAGE_DISPLAY, handler_functions=[self.messages_controller.display_room_messages])
        EventController.add_listener(event_type=EventTypes.ON_SHOW_AVAILABLE_ACTIONS, handler_functions=[self.messages_controller.show_available_actions])

    def pickup_item():
        print("Item has been picked up")
    
    
    def something_that_triggers_itempickup(self):
        EventController.broadcast_event(EventTypes.ON_ITEM_PICKUP)

    def start_game(self):
        EventController.broadcast_event(EventTypes.ON_GAME_START)

    def begin_intro(self):
        self.messages_controller.display_intro_message()

    def initialize_player_settings(self):
        print("Setting up the player settings")

    def initialize_enemy_settings(self):
        print("Initializing the enemy settings")

    def get_mapped_action(self, action) -> Dict[str, str]:
        return action

    def play_dead_message(self):
        message = "Game Over"
        EventController.broadcast_event(EventTypes.ON_MESSAGE_DISPLAY, message=message)
   
    def kill_program(self):
        sys.exit()
    
    def handle_room_event(self):
        pass