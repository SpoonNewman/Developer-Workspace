from Controllers.Environment_controller.Event_Sequence_Manager.Events.SecretShrineEvents import EventsSecretShrineIntro
from Controllers.Environment_controller.Event_Sequence_Manager.story_events_registry import StoryEventsRegistry
from Controllers.Player_Registry_Actions import PlayerStandardActions
from Controllers.EventController import EventController, EventTypes


class StartRoomSequence():
    mapped_possible_actions = {
        "1": PlayerStandardActions.INVESTIGATE.value,
        "2": PlayerStandardActions.KILL_SELF.value,
        "3": PlayerStandardActions.MOVE_FORWARD.value,
    }
    collection_of_events = {
        "shrine_start": EventsSecretShrineIntro()
    }
    
    def __init__(self) -> None:
        pass

    @classmethod
    def handle_sequence(cls):
        EventController.broadcast_event(EventTypes.ON_SHOW_AVAILABLE_ACTIONS, possible_actions=cls.mapped_possible_actions)
        player_input = str(cls.get_player_input())
        cls.trigger_event_sequence(player_input)

    @classmethod
    def get_player_input(cls):
        return input("\nWhat do you choose?")

    @classmethod
    def trigger_event_sequence(cls, player_action: str):
        if cls.mapped_possible_actions[player_action] == PlayerStandardActions.INVESTIGATE.value:
            current_event = StoryEventsRegistry.registry["SecretShrineInvestigation"]
            EventController.broadcast_event(EventTypes.ON_MESSAGE_DISPLAY, message=current_event.description)
            current_event.handle_event()

    @classmethod
    def get_room_possible_actions(cls):
        return {
            "1": PlayerStandardActions.INVESTIGATE.value,
            "2": PlayerStandardActions.KILL_SELF.value,
            "3": PlayerStandardActions.MOVE_FORWARD.value,
        }