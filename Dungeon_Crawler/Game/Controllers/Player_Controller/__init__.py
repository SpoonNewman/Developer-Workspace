from Controllers.base_controller import BaseController
from Controllers.Player_Registry_Actions import PlayerStandardActions




class PlayerController(BaseController):
    #TODO: set whitelist keys to room type enum
    def __init__(self, event_registry) -> None:
        super().__init__(event_registry=event_registry)

    def get_available_actions(self, room):  
        return self.available_actions

    def take_action(self, action_type: str):
        pass
    
    def actions_by_room_type(self, room_type: str):
        return []
        

