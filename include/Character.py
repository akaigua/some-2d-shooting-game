import pygame
import time
import random


# from PIL import Image
# size = Image.open().size


class Player(pygame.sprite.Sprite):
    """the characteristic of character
        speed in x,speed in y,the acceleration of speed in x,the acceleration of speed in y,health point,its strength"""

    def __init__(self, mx, max_hp, strength):  # wtf is Mx
        self.image = pygame.image.load(
            "./assets/character_file_compressed/stand_right.png").convert_alpha()  # the image of player
        self.rect = self.image.get_rect()
        self.w, self.h = pygame.image.load("./assets/character_file_compressed/stand_right.png").get_rect().size
        self.SCREEN_W = 1000
        self.SCREEN_H = int(self.SCREEN_W * 2 / 3)
        # self.x = 0 + self.w
        self.x = 0
        # self.y = self.SCREEN_H - self.h
        self.y = 0
        self.speedx = 5
        self.speedy = 5
        self.hp = max_hp
        self.Mhp = max_hp
        self.distance = self.x - mx
        self.strength = strength

    def move(self, left, right, up):
        if left:
            self.x -= self.speedx
        elif right:
            self.x += self.speedx
        elif up:
            self.y += self.speedy
            time.sleep(0.3)
            self.y -= self.speedy
        else:
            self.x = 0
            # self.y = -self.speedy

        if self.x + self.w > self.SCREEN_W:
            self.x = self.SCREEN_W

        if self.x - self.w < 0:
            self.x = 0

        if self.y + self.h > self.SCREEN_H:
            self.y = self.SCREEN_H

        if self.y - self.h < 0:
            self.y = 0

    def display_direction(self):
        # lack of photo now
        if self.speedx >= 0:
            if self.speedx != 0:
                self.image = pygame.image.load("./assets/character_file_compressed/move_right.png").convert_alpha()
            else:
                self.image = pygame.image.load("./assets/character_file_compressed/stand_right.png").convert_alpha()
            return True
            # towards the right
        elif self.speedx < 0:
            if self.speedx != 0:
                self.image = pygame.image.load("./assets/character_file_compressed/move_left.png").convert_alpha()
            else:
                self.image = pygame.image.load("./assets/character_file_compressed/stand_right.png").convert_alpha()
            return False
            # towards the left

    def attack(self, attack):
        if attack:
            if abs(self.distance) < 25:
                self.Mhp -= self.strength
                time.sleep(round(random.uniform(0.5, 0.8), 3))

    def update(self, Mx, My):
        self.distance = self.x - Mx

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))


'''''
class Monster(pygame.sprite.Sprite):
    def __init__(pic, self, x, y, Px, Py, Php, speedx, hp, strength):
        # The monster would attack the player if their distance is too close or the player has alraedy attack him.
        
        # Monsters would go towards the player when they are in the same layer. 
        #They also go back and forthin their platform.
        ## If the player is shooting at them more than three times, they would go towards the player together.
        #The player won't be allowed to go through the door without shooting all of the monsters.
        
        self.image = pygame.image.load(pic).convert_alpha()  # the image of player
        self.rect = self.image.get_rect()
        self.w, self.h = pygame.image.load().get_rect().size
        self.x, self.y = x, y
        self.distance = self.x - Px
        self.Px, self.Py = Px, Py
        self.Php = Php
        self.speedx = speedx
        self.speedy = 0
        self.hp = hp
        self.strength = strength

    def move(self):
        if self.hp <= 50 or abs(self.distance) < 40:
            # when the monster is angery
            if self.distance >= 0:
                self.speedx += 0.5
            elif self.distance < 0:
                self.speedx -= 0.5
            else:
                self.speedx == 0
        else:
            # walk back and forth when he's peace
            r, l = self.collide
            if r == False or l == False:
                self.speedx *= -1

    def display_direction(self):
        # lack of photo now
        if self.speedX >= 0:
            if self.speed == 0:
                self.image = pass
            else:
                self.image = pass
            return True
            # towards the right
        elif self.speedX < 0:
            if self.speed == 0:
                self.image = pass
            else:
                self.image = pass
            return False 
            # towards the left

    def update(self, Px):
        self.distance = self.x - Px

    def collide(self):
        if self.x + self.w > self.SCREEN_W:
            self.x = self.SCREEN_W
            return  False
        elif self.x - self.w < 0:
            self.x = 0
            return  False
        
        if self.y + self.h > self.SCREEN_H:
            self.y = self.SCREEN_H
        if self.y - self.h < 0:
            self.y = 0       
        return True, True

    def damage(self):
        self.image = pass
        if abs(self.distance) < 25:
            self.Php -= self.strength
            time.sleep(round(random.uniform(0.7, 1), 3))
        

    def draw(self, surface):
        # renderer((self.x, self.y), )
        surface.blit(self.image, (self.x, self.y))


'''''
