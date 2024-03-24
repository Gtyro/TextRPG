import openpyxl

class Enemy:
    def __init__(self, name:str, MHP, attack, defense, money, experience):
        self.name = name
        self.MHP = MHP
        self.HP = MHP
        self.attack = attack
        self.defense = defense
        self.money = money
        self.experience = experience
    
    def info(self):
        return f"Enemy Info: Health - {self.health}, Attack - {self.attack}, Defense - {self.defense}, Money - {self.money}, Experience - {self.experience}"

    def display_info(self):
        print(self.info())
    
    def getHPpct(self):
        return self.HP/self.MHP*100
        
def read_enemy_data_from_excel(filename) -> list[Enemy]:
    try:
        workbook = openpyxl.load_workbook(filename)
        sheet = workbook.active

        enemies = []

        for row in sheet.iter_rows(min_row=2, values_only=True):
            name, health, attack, defense, money, experience = row
            enemy = Enemy(name, health, attack, defense, money, experience)
            enemies.append(enemy)

        return enemies
    except FileNotFoundError:
        print(f"Error: Cannot find file '{filename}'")
        return []

# 从 Excel 表中读取怪物信息
filename = "data/EnemyData.xlsx"
enemies = read_enemy_data_from_excel(filename)
