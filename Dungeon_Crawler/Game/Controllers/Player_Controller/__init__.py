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
    #TODO: set whitelist keys to room type enum
    room_actions_whitelist = {
        "Tunnel": [PlayerStandardActions.MOVE_FORWARD.value, PlayerStandardActions.MOVE_BACKWARD, PlayerStandardActions.JUMP, PlayerStandardActions.CROUCH, PlayerStandardActions.KILL_SELF],
        "Dead end": [PlayerStandardActions.KILL_SELF, PlayerStandardActions.JUMP, PlayerStandardActions.CROUCH, PlayerStandardActions.MOVE_BACKWARD]
    }
    def __init__(self) -> None:
        self.available_actions = []
        for name, member in PlayerStandardActions.__members__.items():
            self.available_actions.append(member.value)

    def get_available_actions(self, room):  
        return self.available_actions

    def take_action(self, action_type: str):
        pass
    
    def actions_by_room_type(self, room_type: str):
        return self.room_actions_whitelist[room_type]
        

