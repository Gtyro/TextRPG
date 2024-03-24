class Weapon:
    def __init__(self, name, attack, price):
        self.name = name
        self.attack = attack
        self.price = price
        
    def info(self):
        return f"Weapon Info: Attack - {self.attack}, Price - {self.price}"

    def display_info(self):
        print(f"Weapon Info: Attack - {self.attack}, Price - {self.price}")
        
woodenSword = Weapon("木剑",2<<2,2<<3)
stoneSword = Weapon("石剑",2<<3,2<<5)
ironSword = Weapon("铁剑",2<<4,2<<7)
steelsword = Weapon("钢剑",2<<5,2<<9)
swords = [woodenSword, stoneSword, ironSword, steelsword]