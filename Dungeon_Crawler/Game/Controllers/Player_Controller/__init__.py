from enum import Enum
from time import sleep
from Controllers.base_controller import BaseController
from Controllers.Player_Registry_Actions import PlayerStandardActions
from Controllers.EventController import EventController, EventTypes
from Controllers.Item_Manager.Item_Registry import ItemRegistry
from Controllers.game_events import OnMessageDisplayEvent, OnSfxPlayEvent, OnPlayerStatChange, OnShowItemActionsEvent
from Controllers.Item_Manager.Adventuring_Items import TorchItem

class PlayerStatusCharacteristic(Enum):
    HEALTH = 0
    MANA = 1
    FAITH = 2

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
    __mana_current = 0
    __faith_current = 0
    __health_current = 0

    max_inventory_capacity = 30
    max_mana_capacity = 80
    max_faith_capacity = 40
    max_health_capacity = 100

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
            player_input = input(f"Are you sure you want to drop {item.name} Y/N:    ")
            if player_input.lower() == "y":
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


    @classmethod
    def __init__(cls) -> None:
        pass

    @classmethod
    def initialize_player_settings(cls, **kwargs):
        game_settings = kwargs.get("settings")
        cls.set_starting_inventory()
        cls.set_starting_stats()
        config_start_room = game_settings["starting_room"]
        starting_room = cls.registered_rooms[config_start_room] if game_settings["starting_room"] else cls.registered_rooms["start_room"]
        cls.set_current_location(location=starting_room)

    @classmethod
    def set_starting_stats(cls):
        for stat in PlayerStatusCharacteristic.__members__.keys():
            evt = OnPlayerStatChange()
            evt.stat_type = stat
            if stat == PlayerStatusCharacteristic.FAITH.name:
                evt.stat_value = cls.max_faith_capacity
            elif stat == PlayerStatusCharacteristic.HEALTH.name:
                evt.stat_value = cls.max_health_capacity
            elif stat == PlayerStatusCharacteristic.MANA.name:
                evt.stat_value = cls.max_mana_capacity
            else:
                evt.stat_value = 1
            EventController.broadcast_event(event_object=evt)

    @classmethod
    def set_stat(cls, event):
        # event = kwargs.get("event_object")
        if event:
            stat_type = event.stat_type
            stat_value = event.stat_value

            if stat_type == PlayerStatusCharacteristic.FAITH:
                cls.set_faith(faith=stat_value)
            elif stat_type == PlayerStatusCharacteristic.HEALTH:
                cls.set_health(health=stat_value)
            elif stat_type == PlayerStatusCharacteristic.MANA:
                cls.set_mana(mana=stat_value)
            else:
                print(f"Didn't understand the stat type: {stat_type}")

    @classmethod
    def set_health(cls, health: int):
        if health <= cls.max_health_capacity:
            cls.__health_current = health
        else:
            cls.__health_current = cls.max_health_capacity

    @classmethod
    def set_mana(cls, mana: int):
        cls.__mana_current = mana

    @classmethod
    def set_faith(cls, faith: int):
        cls.__faith_current = faith

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
        
