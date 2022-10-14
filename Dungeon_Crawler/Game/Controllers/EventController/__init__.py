from enum import Enum
from events import Events

class EventTypes(Enum):
    ON_KILL_SELF = "on_kill_self"
    ON_DIE = "on_die"
    ON_MESSAGE_DISPLAY = "on_message_display"
    ON_ROOM_MESSAGE_DISPLAY = "on_room_message_display"
    ON_SHOW_AVAILABLE_ACTIONS = "on_show_available_actions"
    ON_INTRO_DISPLAY = "on_intro_display"
    ON_GAME_START = "on_game_start"
    ON_PLAYER_ACTION = "on_player_action"
    ON_ITEM_PICKUP = "on_item_pickup"
    ON_PLAYER_INVESTIGATE = "on_player_investigate"

class EventController():
    # valid_event_types = (
    #     EventTypes.ON_DIE.value,
    #     EventTypes.ON_MESSAGE_DISPLAY.value,
    #     EventTypes.ON_ROOM_MESSAGE_DISPLAY.value,
    #     EventTypes.ON_SHOW_AVAILABLE_ACTIONS.value,
    #     EventTypes.ON_PLAYER_INVESTIGATE.value,
    #     EventTypes.ON_KILL_SELF.value,
    #     EventTypes.ON_GAME_START.value,
    #     EventTypes.ON_PLAYER_ACTION.value,
    #     EventTypes.ON_ITEM_PICKUP.value
    # )

    __events = Events((list(map(lambda event: event.value, EventTypes.__members__.values()))))

    @classmethod
    def add_listener(cls, event_type: EventTypes, handler_functions: list):
        event = getattr(cls.__events, event_type.value)
        for handler in handler_functions:
            event += handler

    @classmethod
    def broadcast_event(cls, event_type: EventTypes, **kwargs):
        event = getattr(cls.__events, event_type.value)
        if kwargs == {}:
            event()
        else:
            event(**kwargs)