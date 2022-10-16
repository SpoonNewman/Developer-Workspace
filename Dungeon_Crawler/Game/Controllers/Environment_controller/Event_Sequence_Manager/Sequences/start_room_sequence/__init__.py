from typing import Dict
from Controllers.Environment_controller.Event_Sequence_Manager.Events.SecretShrineEvents import EventsSecretShrineIntro
from Controllers.Environment_controller.Event_Sequence_Manager.story_events_registry import StoryEventsRegistry
from Controllers.Player_Registry_Actions import PlayerStandardActions
from Controllers.EventController import EventController, EventTypes
from Controllers.game_events import OnLocationChangeEvent, OnShowAvailableActionsEvent, OnMessageDisplayEvent, OnKillSelfEvent


class StartRoomSequence():
    mapped_possible_actions = {
        "1": PlayerStandardActions.INVESTIGATE.value,
        "2": PlayerStandardActions.KILL_SELF.value,
        "3": PlayerStandardActions.MOVE_FORWARD.value,
    }
    
    collection_of_events = {
        "shrine_start": EventsSecretShrineIntro()
    }

    @classmethod
    def handle_sequence(cls, room_exits = None, registered_rooms: Dict = {}):
        cls.registered_rooms=registered_rooms
        if room_exits and len(room_exits) > 0:
            cls.room_exits = room_exits
        evt = OnShowAvailableActionsEvent(possible_actions=cls.mapped_possible_actions)
        # EventController.broadcast_event(EventTypes.ON_SHOW_AVAILABLE_ACTIONS, possible_actions=cls.mapped_possible_actions)
        EventController.broadcast_event(event_object=evt)
        player_input = str(cls.get_player_input())
        cls.trigger_event_sequence(player_input)

    @classmethod
    def get_player_input(cls):
        return input("\nWhat do you choose?")

    @classmethod
    def trigger_event_sequence(cls, player_action: str):
        if cls.mapped_possible_actions[player_action] == PlayerStandardActions.INVESTIGATE.value:
            current_event = StoryEventsRegistry.registry["SecretShrineInvestigation"]
            evt = OnMessageDisplayEvent(message=current_event.description)
            EventController.broadcast_event(event_object=evt)
            # EventController.broadcast_event(EventTypes.ON_MESSAGE_DISPLAY, message=current_event.description)
            current_event.handle_event()
        
        elif cls.mapped_possible_actions[player_action] == PlayerStandardActions.KILL_SELF.value:
            evt = OnKillSelfEvent()
            EventController.broadcast_event(event_object=evt)
        
        elif cls.mapped_possible_actions[player_action] == PlayerStandardActions.MOVE_FORWARD.value:
            forward_exit = list(filter(lambda exit: exit in cls.registered_rooms.keys(), cls.room_exits))[0]
            evt = OnLocationChangeEvent(location=cls.registered_rooms[forward_exit])
            # EventController.broadcast_event(EventTypes.ON_LOCATION_CHANGE, event_object=evt)
            EventController.broadcast_event(event_object=evt)
        
        else:
            raise ValueError("We received an unsupported player action {player_action}")


    @classmethod
    def get_room_possible_actions(cls):
        return {
            "1": PlayerStandardActions.INVESTIGATE.value,
            "2": PlayerStandardActions.KILL_SELF.value,
            "3": PlayerStandardActions.MOVE_FORWARD.value,
        }