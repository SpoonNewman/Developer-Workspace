

from Controllers.Environment_controller.Scene_Manager.Events.GoblinAttackEvents import EventsGoblinAttackIntro
from Controllers.Environment_controller.Scene_Manager.Events.SecretShrineEvents import EventsSecretShrineIntro


class SceneEventsRegistry():
    registry = {
        "EasyGoblinAttack": EventsGoblinAttackIntro(),
        "SecretShrineInvestigation": EventsSecretShrineIntro()
    }