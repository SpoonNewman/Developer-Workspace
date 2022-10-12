

from Controllers.Environment_controller.Event_Sequence_Manager.Events.GoblinAttackEvents import EventsGoblinAttackIntro
from Controllers.Environment_controller.Event_Sequence_Manager.Events.SecretShrineEvents import EventsSecretShrineIntro


class StoryEventsRegistry():
    registry = {
        "EasyGoblinAttack": EventsGoblinAttackIntro(),
        "SecretShrineInvestigation": EventsSecretShrineIntro()
    }