from events import Events
from Controllers.game_events import EventTypes

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