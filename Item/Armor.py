class Armor:
    def __init__(self, name, attack, price):
        self.name = name
        self.attack = attack
        self.price = price
        
    def info(self):
        return f"Armor Info: Defence - {self.attack}, Price - {self.price}"

    def display_info(self):
        print(f"Armor Info: Defence - {self.attack}, Price - {self.price}")
        
leatherShield = Armor("皮盾",2<<2,2<<3)
stoneShield = Armor("石盾",2<<3,2<<5)
ironShield = Armor("铁盾",2<<4,2<<7)
steelShield = Armor("钢盾",2<<5,2<<9)
armors = [leatherShield, stoneShield, ironShield, steelShield]