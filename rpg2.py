#! /usr/bin/env python3
# Purpose: Demonstrate class attributes
import random 

class Player:
    loot = 0
    
    def __init__(self, name):
        self.name = name
        self.magic_items  = []
        self.strength     = roll_3_dice()
        self.intelligence = roll_3_dice()
        self.weapon = False
        self.armor  = False
        self.spell  = False
        self.gold   = 0
        
    def get_gold(self, gold):
        self.gold += gold
        Player.loot += gold
        
    def __str__(self):
        s = f'Player {self.name} has ST:{self.strength} IN:{self.intelligence}'
        if self.weapon:
            s += f'Wielding a {self.weapon.name}'
        return s
                    
def main():
    bill  = Player('Corwin')
    sally = Player('Arthur')
    matt  = Player('Sam')
    bill.get_gold(50)
    sally.get_gold(100)
    print(Player.loot)
                
def roll_3_dice():
    total = 0
    for _ in range(3):
        total += random.randrange(1,7)
    return total

if __name__ == "__main__":
    main()
