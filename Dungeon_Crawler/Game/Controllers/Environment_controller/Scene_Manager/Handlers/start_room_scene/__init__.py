from typing import Dict
from Controllers.Player_Registry_Actions import PlayerStandardActions
from Controllers.EventController import EventController, EventTypes
from Controllers.game_events import OnLocationChangeEvent, OnShowAvailableActionsEvent, OnMessageDisplayEvent, OnKillSelfEvent
from Controllers.Player_Registry_Actions import UniversalPlayerActions
from Controllers.Player_Registry_Actions import UniversalPlayerActionKeys
from Controllers.Environment_controller.Scene_Manager.Handlers.Base_Scene_Handler import BaseSceneHandler


class StartRoomScene(BaseSceneHandler):
    description = ["You stand at the entrance to the dungeon in a small hallway. ", "The door behind you is locked and there is only faint illumination. ", "The dungeon entrance is a small archway barely tall enough to walk through."]
    possible_actions = {
        "1": PlayerStandardActions.MOVE_FORWARD.value,
    }

    @classmethod
    def trigger_event(cls, player_state = None):
        if not player_state:
            cls.display_description(description=cls.description)


    @classmethod
    def trigger_event(cls, player_action: str):
        if player_action in cls.possible_actions.keys():
            if cls.possible_actions[player_action] == PlayerStandardActions.MOVE_FORWARD.value:
                move_evt = OnMessageDisplayEvent()
                move_evt.message = "\n\nYou move forward slowly through the room towards the exit."
                EventController.broadcast_event(move_evt)

                forward_exit = list(filter(lambda exit: exit in cls.registered_scenes.keys(), cls.scene_connections))[0]
                evt = OnLocationChangeEvent()
                evt.location = cls.registered_scenes[forward_exit]
                EventController.broadcast_event(evt)
        
        elif player_action in UniversalPlayerActions.actions.keys():
            if player_action != UniversalPlayerActionKeys.LOOK_AROUND.value:
                UniversalPlayerActions.take_action(action=player_action)
            # else:
                cls.display_description(description=cls.description)
            cls.action_input_handler()
        elif cls.possible_actions[player_action] == PlayerStandardActions.LOOK_AROUND.value:
            cls.display_description(description=cls.description)
        else:
            print("That action is unsupported, try again")
            cls.trigger_event(player_action=player_action)