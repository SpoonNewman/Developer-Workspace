from typing import Dict
from Controllers.Environment_controller.Event_Sequence_Manager.Events.SecretShrineEvents import EventsSecretShrineIntro
from Controllers.Environment_controller.Event_Sequence_Manager.story_events_registry import StoryEventsRegistry
from Controllers.Player_Registry_Actions import PlayerStandardActions
from Controllers.EventController import EventController, EventTypes
from Controllers.game_events import OnLocationChangeEvent, OnShowAvailableActionsEvent, OnMessageDisplayEvent, OnKillSelfEvent
from Controllers.Environment_controller.Event_Sequence_Manager.Sequences.Base_Sequence import BaseSequence


class StartRoomSequence(BaseSequence):
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
            setattr(evt, "typewriter_delay", 0.02)
            EventController.broadcast_event(event_object=evt)
            current_event.handle_event()
        
        elif cls.mapped_possible_actions[player_action] == PlayerStandardActions.KILL_SELF.value:
            evt = OnKillSelfEvent()
            EventController.broadcast_event(event_object=evt)
        
        elif cls.mapped_possible_actions[player_action] == PlayerStandardActions.MOVE_FORWARD.value:
            move_evt = OnMessageDisplayEvent()
            move_evt.message = "\n\nYou move forward slowly through the room towards the exit."
            EventController.broadcast_event(event_object=move_evt)

            forward_exit = list(filter(lambda exit: exit in cls.registered_rooms.keys(), cls.room_exits))[0]
            evt = OnLocationChangeEvent()
            evt.location = cls.registered_rooms[forward_exit]
            EventController.broadcast_event(event_object=evt)
        else:
            raise ValueError("We received an unsupported player action {player_action}")