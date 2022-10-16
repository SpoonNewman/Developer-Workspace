from events import Events
from Controllers.game_events import EventTypes

# class EventTypes(Enum):
#     ON_KILL_SELF = "on_kill_self"
#     ON_DIE = "on_die"
#     ON_MESSAGE_DISPLAY = "on_message_display"
#     ON_ROOM_MESSAGE_DISPLAY = "on_room_message_display"
#     ON_SHOW_AVAILABLE_ACTIONS = "on_show_available_actions"
#     ON_INTRO_DISPLAY = "on_intro_display"
#     ON_GAME_START = "on_game_start"
#     ON_PLAYER_ACTION = "on_player_action"
#     ON_ITEM_PICKUP = "on_item_pickup"
#     ON_PLAYER_INVESTIGATE = "on_player_investigate"
#     ON_LOCATION_CHANGE = "on_location_change"

class EventController():
    __events = Events((EventTypes.get_registered_events()))

    @classmethod
    def add_listener(cls, event_type: str, handler_functions: list):
        event = getattr(cls.__events, event_type)
        for handler in handler_functions:
            event += handler

    @classmethod
    def broadcast_event(cls, **kwargs):
        # TODO: Instead of using kwargs here go with the `evt` game event pattern
        # where we create an evt object, assign whatever kwargs we want to that object
        # and pass that in a parameter in this function
        event_object = kwargs.get("event_object")
        event = getattr(cls.__events, event_object.__class__.__name__)
        if kwargs == {}:
            event()
        else:
            event(**kwargs)