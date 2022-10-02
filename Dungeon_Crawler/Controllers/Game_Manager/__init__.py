from typing import Dict
from Controllers.Event_Types import EventTypes
from Controllers.Messages_Controller import MessagesController
from Controllers.Player_Controller import PlayerController
from Controllers.Environment_controller import EnvironmentController
from constants import GameConstants
from events import Events

def initialize_game_controllers():
    return MessagesController(), PlayerController(), EnvironmentController()

class GameManager():
    is_dead: bool = False
    valid_event_types = (EventTypes.ON_DIE.value, EventTypes.ON_KILL_SELF.value, EventTypes.ON_GAME_START.value, EventTypes.ON_PLAYER_ACTION.value, EventTypes.ON_ITEM_PICKUP.value)

    def __init__(self) -> None:
        self.__events = Events((self.valid_event_types))
        self.initialize_events()

        self.messages_controller, self.player_controller, self.environment_controller = initialize_game_controllers() # object1, objec2
        
        self.on_game_start += self.begin_intro
        self.on_game_start += self.initialize_player_settings
        self.on_game_start += self.initialize_enemy_settings
        self.on_item_pickup += self.pickup_item
        # self.on_die += self.play_dead_message
        #
        self.on_player_action += self.player_controller.take_action
        
        self.current_location = GameConstants.player_starting_area # This should probably be a room object instead

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
        self.__events.on_game_start()

    def begin_intro(self):
        self.messages_controller.display_intro_message()

    def initialize_player_settings(self):
        print("Setting up the player settings")

    def initialize_enemy_settings(self):
        print("Initializing the enemy settings")

    def player_take_action(self, current_action):
        # Move forward
        mapped_action = self.get_mapped_action(current_action)
        if mapped_action == "1":
            on_death_message = ["You move forward down the tunnel.", " A spear extends from the wall impaling you through the side upon it's tip.", ".", ".", "You feel the life blood slowly leaking out of you.", "\nYou are", ".", ".", ".", "dead"]
            self.messages_controller.display_room_messages(current_room_messages=on_death_message)
            self.is_dead = True
        
        if not self.is_dead:
            self.__events.on_player_action(current_action)

    def get_mapped_action(self, action) -> Dict[str, str]:
        return action

    # What other things do we initialize?