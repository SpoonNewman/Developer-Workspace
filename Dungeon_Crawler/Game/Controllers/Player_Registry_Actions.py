from enum import Enum

class PlayerStandardActions(Enum):
    KILL_SELF = "Kill Self"
    MOVE_FORWARD = "Move Forward"
    MOVE_BACKWARD = "Move Backward"
    MOVE_LEFT = "Move Left"
    MOVE_RIGHT = "Move Right"
    JUMP = "Jump"
    CROUCH = "Crouch"