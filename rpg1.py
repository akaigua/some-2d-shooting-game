#! /usr/bin/env python3
# Purpose: Demonstrate Objects and Classes
import random 

class Player:
    def __init__(self, name):
        self.name = name
        self.magic_items  = []
        self.strength     = roll_3_dice()
        self.intelligence = roll_3_dice()
        self.weapon = None
        self.armor  = None
        self.spell  = None
        
    def __str__(self):
        s = f'Player {self.name} has ST:{self.strength} IN:{self.intelligence}'
        if self.weapon:
            s += f'Wielding a {self.weapon.name}'
        return s
            
def main():
    party = [Player('Corwin')]
    party.append(Player('Arthur'))
    party.append(Player('Sam'))
    s = 'Party: '
    for p in party:
        s += str(p) + '\n'
    print(s)
                
def roll_3_dice():
    total = 0
    for _ in range(3):
        total += random.randrange(1,7)
    return total

if __name__ == "__main__":
    main()
