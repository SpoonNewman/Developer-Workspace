from enum import Enum


class PlayerStandardActions(Enum):
    KILL_SELF = "Kill Self"
    MOVE_FORWARD = "Move Forward"
    MOVE_BACKWARD = "Move Backward"
    MOVE_LEFT = "Move Left"
    MOVE_RIGHT = "Move Right"
    JUMP = "Jump"
    CROUCH = "Crouch"

class PlayerController():
    def __init__(self) -> None:
        pass

    def get_available_actions(self):
        tmp_list = []
        for name, member in PlayerStandardActions.__members__.items():
            tmp_list.append(member.value)
        return tmp_list

    def take_action(self, action_type: str):
        pass