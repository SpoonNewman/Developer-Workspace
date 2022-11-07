from typing import Dict
from xml.dom.domreg import registered
from Controllers.Environment_controller.Scene_Manager.Handlers.start_room_scene import StartRoomScene
from Controllers.Environment_controller.Scene_Manager.Handlers.SectorA.Some_Room_Scene import SomeRoomScene
from Controllers.Environment_controller.Scene_Manager.Handlers.SectorA.Tunnel_A1_Scene import TunnelA1Scene
from Controllers.Environment_controller.Scene_Manager.Handlers.SectorA.Chamber_A1_Scene import ChamberA1Scene


class SceneHandlerRegistry():
    registry = {
        "start_room_scene": StartRoomScene,
        "tunnel_a1_scene": TunnelA1Scene,
        "chamber_a1_scene": ChamberA1Scene,
        "some_room_scene": SomeRoomScene
    }