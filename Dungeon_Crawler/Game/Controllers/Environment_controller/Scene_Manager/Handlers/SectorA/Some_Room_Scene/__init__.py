from typing import Dict
from Controllers.Player_Registry_Actions import PlayerStandardActions
from Controllers.EventController import EventController, EventTypes
from Controllers.game_events import OnLocationChangeEvent, OnShowAvailableActionsEvent, OnMessageDisplayEvent, OnKillSelfEvent
from Controllers.Environment_controller.Scene_Manager.Handlers.Base_Scene_Handler import BaseSceneHandler
from Controllers.Player_Registry_Actions import UniversalPlayerActions
from Controllers.Environment_controller.Scene_Manager.Handlers.Base_Scene_Handler import BaseSceneHandler


class SomeRoomScene(BaseSceneHandler):
    description = ""
    possible_actions = {
        "1": PlayerStandardActions.KILL_SELF.value,
        "2": PlayerStandardActions.MOVE_BACKWARD.value,
    }

    @classmethod
    def trigger_event(cls, player_state = None):
        if not player_state:
            cls.display_description(description=cls.description)

    @classmethod
    def trigger_event(cls, player_action: str):
        if player_action in cls.possible_actions.keys() and cls.possible_actions[player_action] == PlayerStandardActions.MOVE_BACKWARD.value:
            move_evt = OnMessageDisplayEvent()
            move_evt.message = "\n\nYou move backward slowly through the room towards the exit to where we came from."
            EventController.broadcast_event(move_evt)
            
            forward_exit = list(filter(lambda exit: exit in cls.registered_scenes.keys(), cls.scene_connections))[0]
            
            evt = OnLocationChangeEvent(location=cls.registered_scenes[forward_exit])
            evt.location = cls.registered_scenes[forward_exit]
            EventController.broadcast_event(evt)

        elif player_action in UniversalPlayerActions.actions.keys():
            UniversalPlayerActions.take_action(action=player_action)
            cls.action_input_handler()

        else:
            raise ValueError(f"We received an unsupported player action {player_action}")