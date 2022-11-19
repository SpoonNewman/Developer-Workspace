from Controllers.Environment_controller.Scene_Manager.scene_events_registry import SceneEventsRegistry
from Controllers.EventController import EventController
from Controllers.Player_Registry_Actions import PlayerStandardActions
from Controllers.game_events import OnCurrentEventChange, OnItemPickupEvent
from Controllers.Player_Registry_Actions import ActionRegistry
from Controllers.Environment_controller.Scene_Manager.Handlers.Base_Scene_Handler import BaseSceneHandler
from Controllers.Item_Manager.Adventuring_Items import BookItem
from Controllers.Actions_Manager.simple_actions import MoveForward
from Controllers.Item_Manager.Weapon_Armor_Items import ChestPlateItem

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

    valid_actions = dict(map(lambda item_kv: (item_kv[0].lower(), item_kv[1]), ActionRegistry.valid_actions.items()))
    previous_actions = []
    items = {
        "book": BookItem(name="Mouldering Book", description="An old book that is damp and covererd in mold.", located_in_event=SceneEventsRegistry.registry["SecretShrineInvestigationPart1"]),
        "chestplate": ChestPlateItem(located_in_event=SceneEventsRegistry.registry["SecretShrineInvestigationPart1"])
    }

    valid_directions = ["forward"]

    scene_events = [
        PlayerStandardActions.INVESTIGATE.value.lower(),
        PlayerStandardActions.MOVE_FORWARD.value.lower(),
    ]

    @classmethod
    def handle_scene_events(cls, full_action, current_scene):
        if full_action == PlayerStandardActions.INVESTIGATE.value.lower():
            if current_scene is None:
                return SceneEventsRegistry.registry["SecretShrineInvestigationPart1"]
            else:
                return "You investigate the area around you for additional clues but don't see anything particularly helpful. Perhaps time to review your notes..."
        elif full_action == "pickup book":
            pickup_book_evt = OnItemPickupEvent()
            pickup_book_evt.item = cls.items["book"]
            EventController.broadcast_event(pickup_book_evt)
            cls.items.pop("book")
            cls.record_action(action=full_action, scene=current_scene)
            return SceneEventsRegistry.registry["SecretShrineInvestigationPart2"]
        elif full_action == "pickup chestplate":
            pickup_chestplate_evt = OnItemPickupEvent()
            pickup_chestplate_evt.item = cls.items["chestplate"]
            EventController.broadcast_event(pickup_chestplate_evt)
            cls.items.pop("chestplate")
            cls.record_action(action=full_action, scene=current_scene)
            return current_scene
        elif full_action == PlayerStandardActions.MOVE_FORWARD.value.lower():
            if current_scene.__class__.__name__ == SceneEventsRegistry.registry["SecretShrineInvestigationPart2"].__class__.__name__:
                return SceneEventsRegistry.registry["SecretShrineInvestigationPart3"]
            else:
                return "You move forward into the nearby wall. You find nothing of interest and return back to your previous spot."
            
    @classmethod
    def display_description(cls):
        super().display_description(description=cls.description)

    @classmethod
    def trigger_event(cls, player_action: str, current_scene_event = None):
        # player action will be custom, e.g. `get lantern`, `pickup object`
        player_actions = list(map(lambda action: action.value.lower(), list(dict(PlayerStandardActions.__members__).values())))
        if player_action in player_actions:
            cls.handle_player_input(action=None, object=None, current_scene_event=current_scene_event, raw_action=player_action)
        else:
            input_parts = cls.validate_player_action_length(input=player_action)
            verb, noun = cls.validate_input(input_parts)
            cls.handle_player_input(action=verb, object=noun, current_scene_event=current_scene_event, raw_action=player_action)

    @classmethod
    def validate_input(cls, args):
        verb, noun = None, None
        for valid_arg in (arg for arg in args if arg):
            if valid_arg.lower() in cls.valid_actions.keys():
                verb = valid_arg
            elif valid_arg in cls.items.keys() or valid_arg in cls.valid_directions:
                noun = valid_arg
        return verb, noun

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
            print("Fuck off there's too many verbs or items!")
            return None, None

    @classmethod
    def handle_player_input(cls, action, object, raw_action, current_scene_event = None):
        if action == "pickup":
            if current_scene_event:
                if object:
                    if cls.items.get("book") and object == cls.items["book"].type:
                        if current_scene_event.__class__.__name__ == cls.items["book"].location_scene_event.__class__.__name__:
                            event = cls.handle_scene_events(full_action=raw_action, current_scene=current_scene_event)
                            if event and not isinstance(event, str):
                                event_change_evt = OnCurrentEventChange()
                                event_change_evt.current_event = event
                                EventController.broadcast_event(event_change_evt)
                            pass
                        else:
                            print("There are no books nearby. Try looking closer.")

                    if cls.items.get("chestplate") and object == cls.items["chestplate"].type:
                        if current_scene_event.__class__.__name__ == cls.items["chestplate"].location_scene_event.__class__.__name__:
                            event = cls.handle_scene_events(full_action=raw_action, current_scene=current_scene_event)
                            if event and not isinstance(event, str):
                                event_change_evt = OnCurrentEventChange()
                                event_change_evt.current_event = event
                                EventController.broadcast_event(event_change_evt)
                            pass
                        else:
                            print("Are you blind? There is no chestplate nearby.")
        elif raw_action in cls.scene_events:
            event = cls.handle_scene_events(full_action=raw_action, current_scene=current_scene_event)
            if event and not isinstance(event, str):
                event_change_evt = OnCurrentEventChange()
                event_change_evt.current_event = event
                EventController.broadcast_event(event_change_evt)
            elif event and isinstance(event, str):
                print(event)
            else:
                print("Something got confused, please try again.")
        else:
            print("That action isn't available, please try again")
