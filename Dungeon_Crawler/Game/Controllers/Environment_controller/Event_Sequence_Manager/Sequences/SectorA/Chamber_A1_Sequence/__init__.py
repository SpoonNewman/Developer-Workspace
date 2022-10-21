from typing import Dict
from Controllers.Environment_controller.Event_Sequence_Manager.Sequences.Base_Sequence import BaseSequence
from Controllers.Environment_controller.Event_Sequence_Manager.story_events_registry import StoryEventsRegistry
from Controllers.EventController import EventController
from Controllers.Player_Registry_Actions import PlayerStandardActions
from Controllers.game_events import OnMessageDisplayEvent
from Controllers.Environment_controller.Event_Sequence_Manager.Events.SecretShrineEvents import EventsSecretShrineIntro

class ChamberA1Sequence(BaseSequence):
    room_description = ["\n\nThe room you've entered is a ruined chamber which was once ornate.", " It is a medium sized room with a domed roof, debris and rocks are scattered throughout.", " A wall of bookcases are nearby with mouldering books.", " The remains of a statue stands against the far wall, it's shoulder shorn away.", ".", ".", " It looks down upon you in judgement."]
    mapped_possible_actions = {
        "1": PlayerStandardActions.INVESTIGATE.value,
        "2": PlayerStandardActions.KILL_SELF.value
    }

    collection_of_events = {
        "shrine_start": EventsSecretShrineIntro()
    }

    @classmethod
    def handle_sequence(cls, room_exits = None, registered_rooms: Dict = {}):
        cls.handle(room_exits=room_exits, registered_rooms=registered_rooms, room_description=cls.room_description, mapped_possible_actions=cls.mapped_possible_actions)
        cls.trigger_event_sequence(str(cls.get_player_input()))

    @classmethod
    def trigger_event_sequence(cls, player_action: str):
        if cls.mapped_possible_actions[player_action] == PlayerStandardActions.INVESTIGATE.value:
            current_event = StoryEventsRegistry.registry["SecretShrineInvestigation"]
            evt = OnMessageDisplayEvent(message=current_event.description)
            EventController.broadcast_event(event_object=evt)
            current_event.handle_event()
        else:
            raise ValueError(f"We received an unsupported player action {player_action}")
        