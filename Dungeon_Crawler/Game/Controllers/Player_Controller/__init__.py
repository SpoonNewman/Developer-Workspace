from itertools import accumulate
from Controllers.base_controller import BaseController
from Controllers.Player_Registry_Actions import PlayerStandardActions
from Controllers.EventController import EventController, EventTypes
from Controllers.Item_Manager.Item_Registry import ItemRegistry
from Controllers.game_events import OnMessageDisplayEvent
from Controllers.Item_Manager.Adventuring_Items import TorchItem




class PlayerController(BaseController):
    __is_dead: bool = False
    __current_location = None
    __inventory = []

    max_inventory_capacity = 30

    @classmethod
    def get_current_capacity(cls):
        return accumulate(list(map(lambda item: item.socket_weight, cls.__inventory)))[-1] if cls.__inventory else 0

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
    def set_current_location(cls, **kwargs):
        event = kwargs.get("event_object")
        location = event.location if event and hasattr(event, "location") else kwargs.get("location")

        cls.__current_location = location
        if location:
            location.trigger_room_sequences()

    @classmethod
    def __init__(cls) -> None:
        pass

    @classmethod
    def initialize_player_settings(cls, **kwargs):
        # print("Setting up the player settings")
        cls.set_starting_inventory()
        cls.set_current_location(location=cls.registered_rooms["start_room"])

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
    def pickup_item(cls, **kwargs):
        # On pickup we need to confirm that the item is not already in the inventory
        # Ensure that the item is registered
        # Add the item to the inventory
            # Are we going to handle inventory management?
        event_object = kwargs.get("event_object")
        item = event_object.item
        result = cls.add_to_inventory(item=item)

        if result:
            item_pickup_message = f"\nA {item.name} has been added to your inventory!"
            item_message_evt = OnMessageDisplayEvent()
            item_message_evt.message = item_pickup_message
            EventController.broadcast_event(event_object=item_message_evt)
            pass

    @classmethod
    def display_inventory(cls, **kwargs):
        print("\nINVENTORY\n=========")
        for index, item in enumerate(cls.get_inventory()):
            message = f"{index+1}\t{item.name}\t\t{item.description}"
            item_message_evt = OnMessageDisplayEvent()
            item_message_evt.message = message
            EventController.broadcast_event(event_object=item_message_evt)
        print("\n")
