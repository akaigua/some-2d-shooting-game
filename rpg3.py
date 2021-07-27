#! /usr/bin/env python3
# Purpose: Lecture 9 on Inheritance
import random 
import time

class Player:
    """Represents a player in a role playing game.
    
    Attributes:
    -- name: A string used as the name
    -- magic_items: A list of items carried by the player
    -- strength: 3-18 with higher number meaning more strength
    -- intelligence: 3-18
    -- weapon : False if unarmed.  A Weapon class object
    -- armor : False if unarmored.  An Armor class object
    -- gold : integer representing party treasure carried by this player
    
    Class Attributes:
    -- loot: The total of all publically known treasure on all players
    
    """
    loot = 0
    
    def __init__(self, name):
        """ Initialize with a name.  Rolls dice for ST/IN"""
        self.name = name
        self.health = 100
        self.magic_items  = []
        self.strength     = roll_3_dice()
        self.intelligence = roll_3_dice()
        self.weapon = False
        self.armor  = False
        self.gold   = 0
        
        
    def get_gold(self, gold):
        """Call when player finds gold"""
        self.gold += gold
        Player.loot += gold
        
    def arm(weapon=False, armor=False):
        """Put on armor and/or a weapon.  Call disarm to take off."""
        if not self.weapon:
            self.weapon = weapon
        if not self.armor:
            self.armor = armor

    def dead(self):
        if self.health <= 0:
            return False

    def attack(self):
        punch = random.randint(5)
        attack = self.intelligence * 0.5 + self.strength + punch
        while Monster.dead != False and Player.dead != False:
            Monster.health -= attack
            time.sleep(0.02)

    def win(self):
        if Monster.dead == False:
            return True
        elif Player.dead == False:
            return False
        
    def __str__(self):
        s = f'Player {self.name} has ST:{self.strength} IN:{self.intelligence}'
        if self.weapon:
            s += f'\n  Wielding a {self.weapon.name}'
        return s
        
class Warrior(Player):
    """Warriors fight, and emit a war cry when they do"""

    def __init__(self, name, war_cry):
        """Pass in name and war_cry"""
        Player.__init__(self, name)
        self.war_cry = war_cry
        
    def __str__(self):
        s = Player.__str__(self)
        s = s.replace("Player", "Warrior", 1)
        s += f'\n  And cries "{self.war_cry}" before battle'
        return s
        
        
class NobleWarrior(Warrior):
    """Some warriors have noble titles.  They also have standard war cries"""
    
    KING_WAR_CRY = "It's good to be the king!"
    
    def __init__(self, name, title):
        """Extra attribute is title, printed before name"""
        if title == "King": # Patriarchy
            war_cry = KING_WAR_CRY
        else:
            war_cry = "For the King!"
        Warrior.__init__(self, name, war_cry)
        self.title = title
        
    def promote(self, new_title):
        """Replace old title with a new one"""
        self.title = new_title
        if new_title == "King":
            self.war_cry = NobleWarrior.KING_WAR_CRY
        
    def __str__(self):
        s = Warrior.__str__(self)
        s = s.replace("Warrior", f'Noble Warrior {self.title}', 1)
        return s
        
class Thief(Player):
    """Sticky fingered players.  Some gold stays in their pockets.
    
       Attribute:
       -- personal_loot: gold that isn't seen by the other players."""

    def __init__(self, name):
        Player.__init__(self, name)
        self.personal_loot = 0

    def get_gold(self, gold):
        """Whenever the Thief gains money, 20% goes into personal loot.
           Remaining money is handled normally"""
        keep = gold // 5  # 20% for me
        self.personal_loot += keep
        Player.get_gold(self, gold - keep)
        
    def __str__(self):
        s = Player.__str__(self)
        s = s.replace("Player", "Thief", 1)
        s += f'\n  With personal loot amounting to {self.personal_loot}'
        return s

class Monster:

    def __init__(self,name):
        """ Rolls dice for ST/IN"""
        self.name = name
        self.size = random.randint(2,6)
        self.magic_items  = []
        self.strength     = random.randint(6,20)
        self.weapon = False
        self.armor  = False
        self.health = 150

    def dead(self):
        if self.health <= 0:
            return False

    def attack(self):
        attack = 0.03 * (self.size + 0.5 * self.strength)
        while Monster.dead != False and Player.dead != False:
            Player.health -= attack
            time.sleep(0.028)
 

    def arm(weapon=False, armor=False):
        """Put on armor and/or a weapon.  Call disarm to take off."""
        if not self.weapon:
            self.weapon = weapon
        if not self.armor:
            self.armor = armor
    '''
    def win(self):
        if Player.dead == False:
            return True
    '''

    def __str__(self):
        s = f'Monster {self.name} has SIZE:{self.size} STRENGH:{self.strength}'
        if self.weapon:
            s += f'\n  Wielding a {self.weapon.name}'
        return s

'''''
class Dragon(Monster):
    def __init__(self, name):
        Monster.__init__(self, name)
    
    def return(self):
        if Monster.dead() = 
'''''

def main():
    print('------------------------')
    bill  = Warrior("Corwin", "Kill Everything")
    amy   = NobleWarrior("Actelerious", "Baroness")
    bruce = Thief("Sam")
    bill.get_gold(50)
    amy.get_gold(100)
    bruce.get_gold(200)
    print(bill)
    print(amy)
    print(bruce)
    amy.promote("King")
    print(amy)
    print('Player used to have',Player.loot, 'coins.')
    party = [bill, amy, bruce]
    [p.get_gold(300//3) for p in party]
    print('Player now have',Player.loot, 'coins.')
    print(bruce)
    print('------------------------')
    Ogre  = Monster("Dragan")
    Gobbling   = Monster("Gobbling")
    Dragon = Monster("Dragon")
    print(Ogre)
    print(Gobbling)
    print(Dragon)
    print('------------------------')
    Player.attack and Monster.attack
    if Player.win == True:
        print('Good guys win')
    else:
        print('Monsters win')
    print('------------------------')

                
def roll_3_dice():
    total = 0
    for _ in range(3):
        total += random.randrange(1,7)
    return total

if __name__ == "__main__":
    main()

