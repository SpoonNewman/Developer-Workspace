

from Controllers.Environment_controller.Scene_Manager.Events.GoblinAttackEvents import EventsGoblinAttackIntro
from Controllers.Environment_controller.Scene_Manager.Events.SecretShrineEvents import EventsSecretShrinePart1, EventsSecretShrinePart2, EventsSecretShrinePart3


class SceneEventsRegistry():
    registry = {
        "EasyGoblinAttack": EventsGoblinAttackIntro(),
        "SecretShrineInvestigationPart1": EventsSecretShrinePart1(),
        "SecretShrineInvestigationPart2": EventsSecretShrinePart2(),
        "SecretShrineInvestigationPart3": EventsSecretShrinePart3()
    }