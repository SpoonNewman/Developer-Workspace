import sys
from typing import Dict
from Controllers.Event_Types import EventTypes
from Controllers.Messages_Controller import MessagesController
from Controllers.Player_Controller import PlayerController, PlayerStandardActions
from Controllers.Environment_controller import EnvironmentController

from constants import GameConstants
from events import Events

def initialize_game_controllers():
    return MessagesController(), PlayerController(), EnvironmentController()

class GameManager():
    __is_dead: bool = False
    valid_event_types = (EventTypes.ON_DIE.value, EventTypes.ON_KILL_SELF.value, EventTypes.ON_GAME_START.value, EventTypes.ON_PLAYER_ACTION.value, EventTypes.ON_ITEM_PICKUP.value)

    @property
    def is_dead(self):
        return self.__is_dead

    @is_dead.setter    
    def is_dead(self, status: bool):
        self.__is_dead = status
        if status:
             self.__events.on_die()

    def __init__(self) -> None:
        self.__events = Events((self.valid_event_types))
        self.initialize_events()

        self.messages_controller, self.player_controller, self.environment_controller = initialize_game_controllers()
        
        # TODO: Move these to an initialize_game_events()
        self.on_game_start += self.begin_intro
        self.on_game_start += self.initialize_player_settings
        self.on_game_start += self.initialize_enemy_settings
        self.on_item_pickup += self.pickup_item
        self.on_die_event += self.play_dead_message
        self.on_die_event += self.kill_program
        self.on_player_action += self.player_controller.take_action

        # TODO: Implement the initialization of the room map that contains a linked list of the rooms
        
        # TODO: Set this to be a room object
        self.current_location = GameConstants.player_starting_area

    def initialize_events(self):
        self.on_die_event = self.__events.on_die
        self.on_kill_self = self.__events.on_kill_self
        self.on_game_start = self.__events.on_game_start # targets: list = []
        self.on_player_action = self.__events.on_player_action
        self.on_item_pickup = self.__events.on_item_pickup
    
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

    def player_take_action(self, current_action: str):
        # Move forward
        if current_action == PlayerStandardActions.MOVE_FORWARD.value:
            on_death_message = ["You move forward down the tunnel.", " A spear extends from the wall impaling you through the side upon it's tip.", ".", ".", "You feel the life blood slowly leaking out of you.", "\nYou are", ".", ".", ".", "dead"]
            self.messages_controller.display_room_messages(current_room_messages=on_death_message)
            self.is_dead = True # TODO: Set this as a property and emit & handle the ON_DEATH event for this as well
        
        if not self.is_dead:
            self.__events.on_player_action(current_action)

    def get_mapped_action(self, action) -> Dict[str, str]:
        return action

    def play_dead_message(self):
        message = "Game Over"
        self.messages_controller.display_message(message)
   
    def kill_program(self):
        sys.exit()
    # What other things do we initialize?