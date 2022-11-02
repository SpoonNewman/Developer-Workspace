from Controllers.Environment_controller.Scene_Manager.scene_events_registry import SceneEventsRegistry
from Controllers.EventController import EventController
from Controllers.Player_Registry_Actions import PlayerStandardActions
from Controllers.game_events import OnNextEventChange
from Controllers.Player_Registry_Actions import UniversalPlayerActions
from Controllers.Player_Registry_Actions import VerbRegistry
from Controllers.Environment_controller.Scene_Manager.Handlers.Base_Scene_Handler import BaseSceneHandler

class ChamberA1Scene(BaseSceneHandler):
    description = [
        "\n\nThe room you've entered is a ruined chamber which was once ornate.",
        " It is a medium sized room with a domed roof, debris and rocks are scattered throughout.", 
        " A wall of bookcases are nearby with mouldering books.", 
        " The remains of a statue stands against the far wall, it's shoulder shorn away.", 
        ".",
        ".",
        " It looks down upon you in judgement."
    ]

    valid_actions = dict(map(lambda item_kv: (item_kv[0].lower(), item_kv[1]), VerbRegistry.valid_actions.items()))

    items = {}
    scene_events = {
        PlayerStandardActions.INVESTIGATE.value.lower(): SceneEventsRegistry.registry["SecretShrineInvestigation"]
    }

    @classmethod
    def display_description(cls):
        super().display_description(description=cls.description)

    @classmethod
    def trigger_event_sequence(cls, player_action: str):
        # TODO: player action will be custom, e.g. `get lantern`, `pickup object`
 
        input_parts = cls.validate_player_action_length(input=player_action)
        cls.validate_input(input_parts)

    @classmethod
    def validate_input(cls, args):
        verb, noun = None, None
        for valid_arg in (arg for arg in args if arg):
            if valid_arg.lower() in cls.valid_actions.keys():
                verb = valid_arg
            elif valid_arg in cls.items.keys():
                noun = valid_arg
        # cls.validate_game_item(item=noun)
        cls.handle_player_input(action=verb, item=noun)

    @classmethod
    def validate_player_action_length(cls, input):
        result = input.split(" ")
        if not result or  len(result) == 0:
            raise ValueError("The player input was null, try again.")
        if len(result) == 1:
            return result[0], None
        elif len(result) == 2:
            return result[0], result[1]
        else:
            raise ValueError("Fuck off there's too many verbs or items!")

    @classmethod
    def handle_player_input(cls, action, item):
        if action == "pickup":
            if item == cls.items["book"].type:
                # TODO:
                # You're too far away, move closer
                # add book to inventory
                # any other things
                pass
            else:
                pass
        elif action in cls.scene_events.keys():

            # TODO: Broadcast event - next_event get's set on PlayerController.
            # Then we can do the PlayerController.next_event.handle_event() up in the game loop
            event_change_evt = OnNextEventChange()
            event_change_evt.next_event = cls.scene_events[action]
            EventController.broadcast_event(event_change_evt)
        else:
            # TODO: Player input wasn't understood, please try again
            print("That action wasn't understood, please try again")
            pass
        
