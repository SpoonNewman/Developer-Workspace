from Controllers.Item_Manager.BaseItem import BaseItemRegistry, GameItem


class WeaponItemsRegistry(BaseItemRegistry):
    @classmethod
    def get_registered_items(cls):
        cls.SWORD = SwordItem().__class__.__name__
        cls.KNIFE = KnifeItem().__class__.__name__
        cls.CLUB = ClubItem().__class__.__name__
        cls.FIREARM = FirearmItem().__class__.__name__

        return [
           cls.SWORD,
           cls.KNIFE,
           cls.CLUB,
           cls.FIREARM
        ]

class ArmorItemsRegistry(BaseItemRegistry):
    @classmethod
    def get_registered_items(cls):
        cls.SHIELD = ShieldItem().__class__.__name__
        
        return [
           cls.SHIELD
        ]

class WeaponItem(GameItem):
    def __init__(self) -> None:
        self.inv_socket_weight = 1

class ArmorItem(GameItem):
    pass

class SwordItem(WeaponItem):
    def __init__(self) -> None:
        self.inv_socket_weight = 2

class KnifeItem(WeaponItem):
    pass

class ClubItem(WeaponItem):
    def __init__(self) -> None:
        self.inv_socket_weight = 2

class ShieldItem(ArmorItem):
    pass

class FirearmItem(WeaponItem):
    pass

