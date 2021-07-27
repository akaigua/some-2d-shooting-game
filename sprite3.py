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
    surface.blit(background, (0,0))
    
    mario_group = pygame.sprite.Group()
          
    clock = pygame.time.Clock()  
    while True:
        clock.tick(60)
        quit, click = check_events()
        if quit:
            break
        if click:        
            mario = Mario(click)
            mario_group.add(mario)

        mario_group.clear(surface, background)        
        mario_group.update(window_size_y)
        mario_group.draw(surface)
        pygame.display.flip()

class Mario(pygame.sprite.Sprite):

    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.Surface((29,47))        
        image_surf = pygame.image.load('mario_sprites.png').convert()
        self.image.blit(image_surf, (0,0), (4, 13, 29, 47))
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect(center=pos) 
        
    def update(self, size_y):
        self.rect.move_ip(0,1)
        if self.rect.top > size_y:
            self.kill()
        
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