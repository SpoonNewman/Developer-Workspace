from itertools import accumulate
from time import sleep
from Controllers.base_controller import BaseController
from Controllers.Player_Registry_Actions import PlayerStandardActions
from Controllers.EventController import EventController, EventTypes
from Controllers.Item_Manager.Item_Registry import ItemRegistry
from Controllers.game_events import OnMessageDisplayEvent, OnSfxPlayEvent
from Controllers.Item_Manager.Adventuring_Items import TorchItem
from Controllers.game_events import OnShowItemActionsEvent

class PlayerActionRecord():
    def __init__(self, action, scene):
        self.action = action
        self.scene = scene


class PlayerController(BaseController):
    __is_dead: bool = False
    __current_location = None
    __inventory = []
    __next_event = None
    __current_event = None
    __previous_actions = []
    __visited_locations_events = []
    # __is_show_room_description = True

    max_inventory_capacity = 30

    @classmethod
    def record_action(cls, event = None, action = None, scene = None):
        action = event.action if event else action
        scene = event.scene if event else scene
        record = PlayerActionRecord(action=action, scene=scene)
        cls.__previous_actions.append(record) 

    @classmethod
    def get_current_capacity(cls):
        current_capacity = 0
        if len(cls.__inventory) > 0:
            for item in cls.__inventory:
                current_capacity += item.inv_socket_weight
        return current_capacity
        # return accumulate(list(filter(lambda item: item.inv_socket_weight, cls.__inventory)))[-1] if cls.__inventory else 0

    @classmethod
    def get_inventory(cls):
        return cls.__inventory

    @classmethod
    def add_to_inventory(cls, item):
        current_capacity = cls.get_current_capacity()
        if current_capacity + item.inv_socket_weight < cls.max_inventory_capacity:
            if item.__class__.__name__ in ItemRegistry.get_registered_items():
                cls.__inventory.append(item)
                return True
        else:
            print("Cannot add item to inventory. You are at max capacity.")
            return False

    @classmethod
    def drop_from_inventory(cls, event):
        item = event.item
        selected_item = list(filter(lambda i: i == item, cls.__inventory))
        if selected_item:
            index = cls.__inventory.index(item)
            cls.__inventory.pop(index)
            print(f"You have dropped {item.name} from your satchel")
        #item is removed from inventory

    @classmethod
    def trigger_current_event(cls, scene):
        is_first_visit = False if scene in cls.get_visited_event_location() else True
        if is_first_visit:
            cls.set_visited_event_location(cls.__current_event)
            cls.__current_event.handle_event()

    @classmethod
    def set_visited_event_location(cls, event):
        cls.__visited_locations_events.append(event)

    @classmethod
    def get_visited_event_location(cls):
        return cls.__visited_locations_events

    @classmethod
    def get_current_event(cls, *args, **kwargs):
        return cls.__current_event

    @classmethod
    def set_current_event(cls, event):
        cls.__current_event = event.current_event

    @classmethod
    def set_next_event(cls, event):
        cls.__next_event = event.next_event

    @classmethod
    def get_next_event(cls, *args, **kwargs):
        return cls.__next_event

    # region Class Properties
    @classmethod
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
    def set_current_location(cls, event = None, location = None):
        location = event.location if event and hasattr(event, "location") else location

        cls.__current_location = location
        # if location:
        #     location.trigger_description()


    @classmethod
    def __init__(cls) -> None:
        pass

    @classmethod
    def initialize_player_settings(cls, **kwargs):
        game_settings = kwargs.get("settings")
        cls.set_starting_inventory()
        config_start_room = game_settings["starting_room"]
        starting_room = cls.registered_rooms[config_start_room] if game_settings["starting_room"] else cls.registered_rooms["start_room"]
        cls.set_current_location(location=starting_room)

    @classmethod
    def set_starting_inventory(cls, **kwargs):
        torch = TorchItem()
        cls.add_to_inventory(item=torch)

    @classmethod
    def get_available_actions(cls, room):  
        pass
    
    @classmethod
    def actions_by_room_type(cls, room_type: str):
        return []

    @classmethod
    def pickup_item(cls, event):
        item = event.item
        result = cls.add_to_inventory(item=item)

        if result:
            if item.pickup_sfx_name:
                sfx_evt = OnSfxPlayEvent()
                sfx_evt.sfx_name = item.pickup_sfx_name
                EventController.broadcast_event(sfx_evt)

            item_pickup_message = f"\n\nA {item.name} has been added to your inventory!"
            item_message_evt = OnMessageDisplayEvent()
            item_message_evt.message = item_pickup_message
            EventController.broadcast_event(item_message_evt)

    @classmethod
    def display_inventory(cls, event = None):
        print("\nINVENTORY\n=========")
        sleep(0.8)
        inventory = enumerate(cls.get_inventory())
        for index, item in inventory:
            message = f"{index+1}\t{item.name}\t\t{item.description}"
            print(message)
            sleep(0.5)
            
        print("\n")
        player_input = input("Choose a number to select the item (q to exit inventory):    ")
        if player_input != "q":
            cls.select_inventory_item(cls.get_inventory()[int(player_input)-1])

    @classmethod
    def select_inventory_item(cls, item):
        item_message_evt = OnMessageDisplayEvent()
        item_message_evt.message = f"You have selected {item.name}"
        EventController.broadcast_event(item_message_evt)
        
        evt = OnShowItemActionsEvent()
        evt.possible_actions = item.actions
        EventController.broadcast_event(evt)

        player_input = str(input("Choose an action:    "))
        item.use_item(action_input=player_input)
        
