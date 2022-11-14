from typing import Dict
from Controllers.EventController import EventController
from Controllers.Player_Registry_Actions import PlayerStandardActions, UniversalPlayerActions, UniversalPlayerActionKeys
from Controllers.game_events import OnMessageDisplayEvent, OnLocationChangeEvent
from Controllers.Environment_controller.Scene_Manager.Handlers.Base_Scene_Handler import BaseSceneHandler


class TunnelA1Scene(BaseSceneHandler):
    description = ["\n\nYou stand in near darkness within a rough hewn tunnel made from natural stone and hand laid brick.", " The air is damp and musty.", " A cool breeze blows and you sense a presence like night itself drawing you further into the tunnel."]
    possible_actions = {
        "1": PlayerStandardActions.MOVE_FORWARD.value,
    }

    @classmethod
    def trigger_event(cls, player_state = None):
        if not player_state:
            cls.display_description(description=cls.description)

    @classmethod
    def trigger_event(cls, player_action: str):
        if player_action in cls.possible_actions.keys() and cls.possible_actions[player_action] == PlayerStandardActions.MOVE_FORWARD.value:
            move_evt = OnMessageDisplayEvent()
            move_evt.message = "\n\nYou move forward slowly through the room towards the exit."
            EventController.broadcast_event(move_evt)

            forward_exit = list(filter(lambda exit: exit in cls.registered_scenes.keys(), cls.scene_connections))[0]
            evt = OnLocationChangeEvent()
            evt.location = cls.registered_rooms[forward_exit]
            EventController.broadcast_event(evt)

        elif player_action in UniversalPlayerActions.actions.keys():
            if player_action != UniversalPlayerActionKeys.LOOK_AROUND.value:
                UniversalPlayerActions.take_action(action=player_action)
            else:
                cls.display_description(description=cls.description)
            cls.action_input_handler()
        else:
            raise ValueError(f"We received an unsupported player action {player_action}")