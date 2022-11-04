from Controllers.Actions_Manager.simple_actions import Jump, Investigate, Pickup, MoveForward

class ActionsManager():
    actions = {
        Investigate().__class__.__name__: Investigate,
        Jump().__class__.__name__: Jump,
        Pickup().__class__.__name__: Pickup,
        MoveForward().__class__.__name__: MoveForward
    }
