import sys
from typing import Dict
from Controllers.Event_Types import EventTypes
from Controllers.Messages_Controller import MessagesController
from Controllers.Player_Controller import PlayerController, PlayerStandardActions
from Controllers.Environment_controller import EnvironmentController

from constants import GameConstants
from events import Events

def initialize_game_controllers(event_registry):
    return MessagesController(event_registry=event_registry), PlayerController(event_registry=event_registry), EnvironmentController(event_registry=event_registry)

class GameManager():
    __is_dead: bool = False
    __current_location = None
    valid_event_types = (EventTypes.ON_DIE.value, EventTypes.ON_KILL_SELF.value, EventTypes.ON_GAME_START.value, EventTypes.ON_PLAYER_ACTION.value, EventTypes.ON_ITEM_PICKUP.value)

    @property
    def is_dead(self):
        return self.__is_dead

    @is_dead.setter    
    def is_dead(self, status: bool):
        self.__is_dead = status
        if status:
             self.__events.on_die()

    @property
    def current_location(self):
        return self.__current_location

    @current_location.setter    
    def current_location(self, location):
        self.__current_location = location
        if location:
            location.trigger_room_sequences()

    
    def __init__(self) -> None:
        self.__events = Events((self.valid_event_types))
        self.initialize_event_subscriptions()
        self.messages_controller, self.player_controller, self.environment_controller = initialize_game_controllers(event_registry=self.__events)
        self.initialize_game_room_map()
        self.current_location = self.environment_controller.registered_rooms["start_room"]
    
    def process_game_interval(self):
        """Process an interval of actions within the game.
        """
        # current_actions = self.messages_controller.show_available_actions(game_manager.player_controller, None)
        # self.current_location.get_available_actions()
        current_action_input = input("Make your selection:  ") # Show Prompt of things they can do
        # self.player_take_action(current_actions[current_action_input])
    
    def initialize_game_room_map(self):
        self.environment_controller.initialize_rooms()

    def initialize_event_subscriptions(self):
        """Initialize the events and their subscriptions.
        """
        self.__events.on_game_start += self.begin_intro
        self.__events.on_game_start += self.initialize_player_settings
        self.__events.on_game_start += self.initialize_enemy_settings
        self.__events.on_item_pickup += self.pickup_item
        self.__events.on_die += self.play_dead_message
        self.__events.on_die += self.kill_program
        # self.__events.on_player_action += self.player_controller.take_action
        # self.__events.on_room_event += self.handle_room_event

    def pickup_item():
        print("Item has been picked up")
    
    
    def something_that_triggers_itempickup(self):
        self.__events.on_item_pickup()

    def start_game(self):
        # TODO: Probably need to move the while loop into this maybe?
        self.__events.on_game_start()

    def begin_intro(self):
        self.messages_controller.display_intro_message()

    def initialize_player_settings(self):
        print("Setting up the player settings")

    def initialize_enemy_settings(self):
        print("Initializing the enemy settings")

    # def player_take_action(self, current_action: str):
    #     # Move forward
    #     if current_action == PlayerStandardActions.MOVE_FORWARD.value:
    #         on_death_message = ["You move forward down the tunnel.", " A spear extends from the wall impaling you through the side upon it's tip.", ".", ".", "You feel the life blood slowly leaking out of you.", "\nYou are", ".", ".", ".", "dead"]
    #         self.messages_controller.display_room_messages(current_room_messages=on_death_message)
    #         self.is_dead = True # TODO: Set this as a property and emit & handle the ON_DEATH event for this as well
        
    #     if not self.is_dead:
    #         self.__events.on_player_action(current_action)

    def get_mapped_action(self, action) -> Dict[str, str]:
        return action

    def play_dead_message(self):
        message = "Game Over"
        self.messages_controller.display_message(message)
   
    def kill_program(self):
        sys.exit()
    
    def handle_room_event(self):
        pass