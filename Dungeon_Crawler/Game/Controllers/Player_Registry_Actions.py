from enum import Enum
from Controllers.EventController import EventController
from Controllers.game_events import OnKillSelfEvent, OnInventoryDisplay, OnPrayEvent
from Controllers.Actions_Manager import ActionsManager

class ActionRegistry():
    valid_actions = ActionsManager.actions
    
    one_word_actions = [
        "jump",
        "crouch",
        "pray",
        "blaspheme",
        "investigate",
    ]

    item_interactive_actions = []

    movement_actions = []

class PlayerStandardActions(Enum):
    KILL_SELF = "Kill Self"
    MOVE_FORWARD = "Move Forward"
    MOVE_BACKWARD = "Move Backward"
    MOVE_LEFT = "Move Left"
    MOVE_RIGHT = "Move Right"
    JUMP = "Jump"
    CROUCH = "Crouch"
    PRAY = "Pray"
    BLASPHEME = "Blaspheme"
    INVESTIGATE = "Investigate"
    ACTIVATE_SWITCH = "Activate Switch"
    # PICKUP_BOOK = "Pickup Book"
    INVENTORY = "Inventory"
    LOOK_AROUND = "Look Around"

class UniversalPlayerActionKeys(Enum):
    KILL_SELF = "k"
    PRAY = "p"
    INVENTORY = "i"
    LOOK_AROUND = "l"

class UniversalPlayerActions():
    actions = {
        UniversalPlayerActionKeys.KILL_SELF.value : PlayerStandardActions.KILL_SELF.value,
        UniversalPlayerActionKeys.PRAY.value : PlayerStandardActions.PRAY.value,
        UniversalPlayerActionKeys.INVENTORY.value : PlayerStandardActions.INVENTORY.value,
        UniversalPlayerActionKeys.LOOK_AROUND.value : PlayerStandardActions.LOOK_AROUND.value
    }

    @classmethod
    def take_action(cls, action: str):
        evt = None
        if cls.actions[action] == PlayerStandardActions.KILL_SELF.value:
            evt = OnKillSelfEvent()
        elif cls.actions[action] == PlayerStandardActions.INVENTORY.value:
            evt = OnInventoryDisplay()
        elif cls.actions[action] == PlayerStandardActions.PRAY.value:
            evt = OnPrayEvent()
            
        EventController.broadcast_event(evt)