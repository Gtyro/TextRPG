from Item.Weapon import Weapon
from Item.Armor import Armor

class Character:
    def __init__(self, name, level, MHP, weapon:Weapon=None, armor:Armor=None, gold=20, experience=0):
        self.name = name
        self.level = level
        self.weapon = weapon
        self.armor = armor
        self.MHP = MHP
        self.HP = MHP

    def info(self):
        weapon_info = f"Weapon: {self.weapon.name}" if self.weapon else "No weapon equipped"
        armor_info = f"Armor: {self.armor.name}" if self.armor else "No armor equipped"
        return f"Character Info:\nName: {self.name}\nLevel: {self.level}\nMHP: {self.MHP}\n{weapon_info}\n{armor_info}\nExperience: {self.experience}"
    
    def getHPpct(self):
        return self.HP/self.MHP*100


# 创建一个人物实例并装备武器和防具
player = Character("Player", 1, 100, experience=0)

# # 打印人物信息
print(player.weapon)
