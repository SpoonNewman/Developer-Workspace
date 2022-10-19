from typing import Dict
from xml.dom.domreg import registered
from Controllers.Environment_controller.Event_Sequence_Manager.Sequences.start_room_sequence import StartRoomSequence
from Controllers.Environment_controller.Event_Sequence_Manager.Sequences.SectorA.Some_Room_Sequence import SomeRoomSequence


class StorySequencesRegistry():
    registry = {
        "start_room_sequence": StartRoomSequence,
        "some_room_sequence": SomeRoomSequence
    }