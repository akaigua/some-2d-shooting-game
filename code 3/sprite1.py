#! /usr/bin/env python3
''' An example of sprites: Mario is a sprite '''
import pygame

def main():
    pygame.init()
    window_size_x = 1200
    window_size_y = 622
    surface = pygame.display.set_mode([window_size_x,window_size_y]) 
    pygame.display.set_caption('Mario as a Sprite')
    background = pygame.image.load('mario_background.png').convert()
    
    mario = Mario((100, 200))
            
    while True:
        quit, click = check_events()
        if quit:
            break
                
        mario.update(click)
        
        surface.blit(background, (0,0))
        mario.draw(surface)
        pygame.display.flip()

class Mario(pygame.sprite.Sprite):

    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.Surface((29,47))        
        image_surf = pygame.image.load('mario_sprites.png').convert()
        self.image.blit(image_surf, (0,0), (4, 13, 29, 47))
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect(topleft=pos)     
        
    def update(self, click):
        if click:
            self.rect.center = click
        
    def draw(self, surface):
        surface.blit(self.image, self.rect)

def check_events():
    ''' A controller of sorts.  Looks for Quit, several simple events.
        Returns: True/False for if a Quit event happened.
    '''
    
    quit = False
    click = None
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                quit = True
            if event.key == pygame.K_ESCAPE:
                quit = True
        if event.type == pygame.MOUSEBUTTONUP:
            click = event.pos
                
    return quit, click

if __name__ == "__main__":
    main()