from typing import Dict
from xml.dom.domreg import registered
from Controllers.Environment_controller.Event_Sequence_Manager.Sequences.start_room_sequence import StartRoomSequence
from Controllers.Environment_controller.Event_Sequence_Manager.Sequences.SectorA.Some_Room_Sequence import SomeRoomSequence
from Controllers.Environment_controller.Event_Sequence_Manager.Sequences.SectorA.Tunnel_A1_Sequence import TunnelA1Sequence
from Controllers.Environment_controller.Event_Sequence_Manager.Sequences.SectorA.Chamber_A1_Sequence import ChamberA1Sequence


class StorySequencesRegistry():
    registry = {
        "start_room_sequence": StartRoomSequence,
        "tunnel_a1_sequence": TunnelA1Sequence,
        "chamber_a1_sequence": ChamberA1Sequence,
        "some_room_sequence": SomeRoomSequence
    }