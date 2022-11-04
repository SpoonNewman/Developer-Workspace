from abc import abstractmethod
from typing import Dict
from Controllers.EventController import EventController

from Controllers.game_events import OnStaggeredMessageDisplayEvent, OnRecordPlayerAction, OnMessageDisplayEvent

class BaseSceneHandler():
    @classmethod
    @abstractmethod
    def handle_scene():
        raise NotImplementedError("This is using base class abstract property, please make your own!")

    @classmethod
    @abstractmethod
    def trigger_event():
        raise NotImplementedError("This is using base class abstract property, please make your own!")

    @classmethod
    def display_description(cls, description: list[str] = None):
        evt = OnStaggeredMessageDisplayEvent()
        evt.messages = description
        EventController.broadcast_event(evt)
 
    @classmethod
    def setup_rooms(cls, room_exits = None, registered_rooms: Dict = {}, room_description: list[str] = None):
        cls.registered_rooms=registered_rooms
        if room_exits and len(room_exits) > 0:
            cls.room_exits = room_exits

    @classmethod
    def record_action(cls, action, scene):
        evt = OnRecordPlayerAction()
        evt.action = action
        evt.scene = scene
        EventController.broadcast_event(evt)

    @classmethod
    def get_player_input(cls):
        evt = OnMessageDisplayEvent()
        evt.message = "\nWhat do you choose?  "
        evt.typewriter_display = 0
        EventController.broadcast_event(evt)

        # Do an event loop and grab the input, then return it
        # while True:
        #     input_obj = TextInput()
        #     user_input = input_obj.get_input()
        #     del input_obj
        #     return user_input