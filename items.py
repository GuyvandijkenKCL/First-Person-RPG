class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Armour(Item):
    def __init__(self, name, description, defence):
        super().__init__(name, description)
        self.defence = defence

class Helmet(Armour):
    def __init__(self, name, description, defence):
        super().__init__(name, description, defence)

class Body(Armour):
    def __init__(self, name, description, defence):
        super().__init__(name, description, defence) 

class Weapon(Item):
    def __init__(self, name, description, attack):
        super().__init__(name, description)
        self.attack = attack