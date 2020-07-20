from random import randint
import math

class Character:
    def __init__(self):
        attributes = ['strength', 'dexterity', 'constitution','intelligence', 'wisdom', 'charisma']
        for _, k in enumerate(attributes):
            setattr(self, k, roll_dices_ability())
        setattr(self, 'hitpoints', 10 + modifier(self.constitution))

    def ability(self):
        return roll_dices_ability()

def modifier(score):
    score =  score - 10
    if score % 2 != 0:
        return int((score -1) / 2)
    return int(score / 2)

def roll_d6():
    return randint(1,6)

def roll_dices_ability():
    dices = []
    for _ in range(4):
        dices.append(roll_d6())
    return sum(sorted(dices)[1:4])
