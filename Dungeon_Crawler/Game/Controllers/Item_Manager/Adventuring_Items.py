from Game.Controllers.Item_Manager.BaseItem import BaseItemRegistry, GameItem


class AdventuringItemsRegistry(BaseItemRegistry):
    @classmethod
    def get_registered_items(cls):
        cls.TORCH = TorchItem().__class__.__name__
        cls.CHEST = ChestItem().__class__.__name__
        cls.CHAIN = ChainItem().__class__.__name__
        cls.ROPE = RopeItem().__class__.__name__

        return [
           cls.TORCH,
           cls.CHEST,
           cls.CHAIN,
           cls.ROPE 
        ]

class AdventuringItem(GameItem):
    pass

class TorchItem(AdventuringItem):
    pass

class ChestItem(AdventuringItem):
    pass

class ChainItem(AdventuringItem):
    pass

class RopeItem(AdventuringItem):
    pass