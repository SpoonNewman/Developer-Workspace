from typing import Dict
from Controllers.Environment_controller.Event_Sequence_Manager.Events.SecretShrineEvents import EventsSecretShrineIntro
from Controllers.Environment_controller.Event_Sequence_Manager.story_events_registry import StoryEventsRegistry
from Controllers.Player_Registry_Actions import PlayerStandardActions
from Controllers.EventController import EventController, EventTypes
from Controllers.game_events import OnLocationChangeEvent, OnShowAvailableActionsEvent, OnMessageDisplayEvent, OnKillSelfEvent
from Controllers.Environment_controller.Event_Sequence_Manager.Sequences.Base_Sequence import BaseSequence
from Controllers.Player_Registry_Actions import UniversalPlayerActions


class StartRoomSequence(BaseSequence):
    mapped_possible_actions = {
        "1": PlayerStandardActions.MOVE_FORWARD.value,
    }

    @classmethod
    def handle_sequence(cls, room_exits = None, registered_rooms: Dict = {}):
        cls.setup_rooms(room_exits=room_exits, registered_rooms=registered_rooms)
        cls.action_input_handler()

    @classmethod
    def action_input_handler(cls):
        player_input = cls.handle_actions(mapped_possible_actions=cls.mapped_possible_actions)
        cls.trigger_event_sequence(player_action=player_input)

    @classmethod
    def trigger_event_sequence(cls, player_action: str):
        if player_action in cls.mapped_possible_actions.keys() and cls.mapped_possible_actions[player_action] == PlayerStandardActions.MOVE_FORWARD.value:
            move_evt = OnMessageDisplayEvent()
            move_evt.message = "\n\nYou move forward slowly through the room towards the exit."
            EventController.broadcast_event(move_evt)

            forward_exit = list(filter(lambda exit: exit in cls.registered_rooms.keys(), cls.room_exits))[0]
            evt = OnLocationChangeEvent()
            evt.location = cls.registered_rooms[forward_exit]
            EventController.broadcast_event(evt)
        
        elif player_action in UniversalPlayerActions.actions.keys():
            UniversalPlayerActions.take_action(action=player_action)
            cls.action_input_handler()
        else:
            raise ValueError(f"We received an unsupported player action {player_action}")