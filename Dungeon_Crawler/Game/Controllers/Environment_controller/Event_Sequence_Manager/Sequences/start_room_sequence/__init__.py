from Controllers.Environment_controller.Event_Sequence_Manager.Events.SecretShrineEvents import EventsSecretShrineIntro
from Controllers.Environment_controller.Event_Sequence_Manager.story_events_registry import StoryEventsRegistry
from Controllers.Player_Registry_Actions import PlayerStandardActions
from Controllers.EventController import EventController, EventTypes


class StartRoomSequence():
    def __init__(self) -> None:
        self.collection_of_events = {
            "shrine_start": EventsSecretShrineIntro()
        }


    def handle_sequence(self):
        self.possible_actions = self.get_room_possible_actions()
        print("\n\n")
        for index, action in enumerate(self.possible_actions):
            pass
            EventController.broadcast_event(EventTypes.ON_MESSAGE_DISPLAY, message=f"{index + 1} - {action}\n")

        player_input = str(self.get_player_input())
        self.trigger_event_sequence(player_input)

    def get_player_input(self):
        return input("\nWhat do you choose?")

    def trigger_event_sequence(self, player_action: str):
        # TODO: match this to the PlayerStandardActions
        if player_action == "1":
            current_event = StoryEventsRegistry.registry["SecretShrineInvestigation"]
            EventController.broadcast_event(EventTypes.ON_MESSAGE_DISPLAY, message=current_event.description)
            current_event.handle_event()

    def get_room_possible_actions(self):
        return [
            PlayerStandardActions.INVESTIGATE.value,
            PlayerStandardActions.KILL_SELF.value,
            PlayerStandardActions.MOVE_FORWARD.value,
        ]