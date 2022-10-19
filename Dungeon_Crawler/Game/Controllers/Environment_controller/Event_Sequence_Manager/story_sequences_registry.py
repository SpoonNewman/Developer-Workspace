from typing import Dict
from xml.dom.domreg import registered
from Controllers.Environment_controller.Event_Sequence_Manager.Sequences.start_room_sequence import StartRoomSequence


class StorySequencesRegistry():
    registry = {
        "start_room_sequence": StartRoomSequence
    }