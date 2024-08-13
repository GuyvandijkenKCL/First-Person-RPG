from items import Helmet, Body, Weapon

class Character:
    def __init__(self, name, level, hp, mp, strength, magic, intelligence, vitality, agility, luck, sprite, skills):
        self.level = level
        self.name = name
        
        self.maxHP = hp 
        self.currentHP = hp
        self.maxMP = mp
        self.currentMP = mp

        self.strength = strength
        self.magic = magic
        self.intelligence = intelligence
        self.vitality = vitality
        self.agility = agility
        self.luck = luck
        self.sprite = sprite
        self.skills = skills

        self.physAttack = self.strength
        self.magAttack = self.magic + self.intelligence / 2

        self.physDefence = self.vitality
        self.magDefence = self.magic + self.vitality / 4

class Human(Character):
    def __init__(self, name, level, hp, mp, strength, magic, intelligence, vitality, agility, luck, sprite, skills, helmet, body, weapon):
        super().__init__(name, level, hp, mp, strength, magic, intelligence, vitality, agility, luck, sprite, skills)

        self.weapon = weapon
        self.helmet = helmet
        self.body = body

        self.basePhysAttack = self.physAttack
        self.baseMagAttack = self.magAttack

        self.basePhysDefence = self.physDefence
        self.baseMagDefence = self.magDefence
        
        self.set_stats()

    def set_stats(self):
        self.physAttack = self.basePhysAttack + self.weapon.attack
        self.physDefence = self.basePhysDefence + self.helmet.defence + self.body.defence
