from Controllers.Actions_Manager.base_action import BaseAction

class Investigate(BaseAction):
    pass

class Jump(BaseAction):
    pass

class Crouch(BaseAction):
    pass

class Pray(BaseAction):
    pass

class Sneak(BaseAction):
    pass

class Hide(BaseAction):
    pass

class Blaspheme(BaseAction):
    pass

class Analyze(BaseAction):
    pass

class Pickup(BaseAction):
    pass

class Grab(BaseAction):
    pass

class Retrieve(BaseAction):
    pass

class Grasp(BaseAction):
    pass

class Hold(BaseAction):
    pass

class Press(BaseAction):
    # Press switch
    pass

class Push(BaseAction):
    pass

class MoveForward(BaseAction):
    def __init__(self):
        self.__class__.__name__ = "Move Forward"