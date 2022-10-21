from Game.Controllers.Item_Manager.BaseItem import BaseItemRegistry, GameItem


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
    pass

class ArmorItem(GameItem):
    pass

class SwordItem(WeaponItem):
    pass

class KnifeItem(WeaponItem):
    pass

class ClubItem(WeaponItem):
    pass

class ShieldItem(ArmorItem):
    pass

class FirearmItem(WeaponItem):
    pass

