#! /usr/bin/env python3
''' Play a simple drop game.
'''
import sys, random
import pygame
import pygame.locals
import pygame.time

def main():
    WINDOW_WIDTH  = 400
    WINDOW_HEIGHT = 600
        
    pygame.init()
    surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Drop!')

    platforms = PlatformManager(WINDOW_WIDTH, WINDOW_HEIGHT)
    redbox    = Avatar(platforms, WINDOW_WIDTH, WINDOW_HEIGHT)
    events    = Controller()

    start_time = pygame.time.get_ticks()
    clock = pygame.time.Clock()
    while events.running:
        clock.tick(30)
        events.check_events()
        
        platforms.update()
        if redbox.update(events.left, events.right):
            break 

        surface.fill((0,0,0))
        platforms.draw(surface)
        redbox.draw(surface)
    
        pygame.display.update()
    
    score = (pygame.time.get_ticks() - start_time)/1000
    print(f'You survived for {score} seconds')

class PlatformManager:
    ''' Container for the platforms.  Allows a single collision question
        to be asked of all the platforms.
    '''
    
    DELAY_DECREASE =  50  # Delay will decrease this much with each new platform
    FASTEST_DELAY  = 700  # ... until it hits this number

    def __init__(self, window_width, window_height):
        self.window_width  = window_width
        self.window_height = window_height
        self.platforms = []
        self.delay = 2000         # New platform starts up every 2000 microseconds
        self.time_of_last_platform = 0
        
    def collision(self, avatar_rect):
        ''' Check collision with all platforms.  Pass the return value
            from the platform.collision function to the caller.
        '''
        for platform in self.platforms:
            collided = platform.collision(avatar_rect)
            if collided:
                return collided
        return None

    def update(self):
        done_platform = False
        for platform in self.platforms:
            if not platform.update():
                done_platform = platform
        if done_platform:
            self.platforms.remove(done_platform)

        if pygame.time.get_ticks() - self.time_of_last_platform > self.delay:
            self.time_of_last_platform = pygame.time.get_ticks()
            self.delay = max(PlatformManager.FASTEST_DELAY, 
                             self.delay - PlatformManager.DELAY_DECREASE)
            new_platform = Platform(self.window_width, self.window_height)
            self.platforms.append(new_platform)

    def draw(self, surface):
        for platform in self.platforms:
            platform.draw(surface)
                       
class Platform:
    ''' Platforms start from the bottom of the screen and move up.  Each
        has a gap through which the Avatar can fall.
    '''
    
    # Class variables!
    THICKNESS = 10
    GAP_WIDTH = 40
    SPEED = 3
    
    def __init__(self, window_width, window_height):
        self.window_width  = window_width
        self.window_height = window_height
        gap_x = random.randint(0, window_width - Platform.GAP_WIDTH)
        gap_end_x = gap_x + Platform.GAP_WIDTH
        self.left_rect = pygame.Rect((0, window_height), (gap_x, Platform.THICKNESS))
        self.right_rect = pygame.Rect((gap_end_x, window_height), 
                                      (window_width - gap_end_x + 1, Platform.THICKNESS))

    def collision(self, a_rect):
        ''' There are two collision scenarios.
            1) The avatar should be riding on this platform.  Detect this by
               checking the avatar's bottom left point is inside the left_rect
               or if the avatar's bottom right point is inside the right_rect
            2) The avatar is inside the gap and trying to move left/right into
               the platform bars.  Detect this (after #1) by checking for a
               rect collision with the avatar.
               
            returns: False if no collision.  Tuple of ('up', y_value) for #1.
                     Tuple of ('left', gap_x) if #2 and hitting the left_rect
                     Tuple of ('right', gap_end_x) if #2 and hitting right
        '''
        if self.left_rect.collidepoint(a_rect.bottomleft):
            return ('up', self.left_rect.top)
        if self.right_rect.collidepoint(a_rect.bottomright):
            return ('up', self.left_rect.top)
        if self.left_rect.colliderect(a_rect):
            return ('left', self.left_rect.right)
        if self.right_rect.colliderect(a_rect):
            return ('right', self.right_rect.left)
        return False
        
    def update(self):
        ''' Platform just needs to move up with each update.
        
            Returns: False when the platform's bottom is no longer viewable.
        '''
        self.left_rect.move_ip(0, -Platform.SPEED)
        self.right_rect.move_ip(0, -Platform.SPEED)
        return self.left_rect.bottom >= 0
        
    def draw(self, surface):
        ''' Draw the platform.
        '''
        pygame.draw.rect(surface, (255,255,255), self.left_rect)
        pygame.draw.rect(surface, (255,255,255), self.right_rect)
        
class Avatar:

    WIDTH  =  10
    HEIGHT =  25
    V_X    =   5
    V_Y    =   3
    
    def __init__(self, platform_mgr, window_width, window_height):
        self.platform_mgr = platform_mgr
        self.window_width  = window_width
        self.window_height = window_height
        self.rect = pygame.Rect((window_width/2 - Avatar.WIDTH, 1),
                                (Avatar.WIDTH, Avatar.HEIGHT))
        
    def update(self, left, right):
        # Update the x position
        if left:
            self.rect.left = max(0, self.rect.left - Avatar.V_X)
        if right:
            self.rect.right = min(self.rect.right + Avatar.V_X, self.window_width)
        
        #update y: Check to see if riding/hitting a platform
        hit = self.platform_mgr.collision(self.rect)
        if hit:
            if hit[0] == 'up':
                self.rect.bottom = hit[1]
            elif hit[0] == 'left':
                self.rect.left = hit[1]
            elif hit[0] == 'right':
                self.rect.right = hit[1]
            else:
                raise('Something stupid happened')       
        else:
            self.rect.y += Avatar.V_Y
        
        if self.rect.y < 0:
            return True
            
        if self.rect.bottom > self.window_height:
            return True
            
        return False  # not dead yet

    def draw(self, surface):
        pygame.draw.rect(surface, (255,0,0), self.rect)
    
class Controller:

    def __init__(self):
        self.left    = False
        self.right   = False
        self.running = True
        
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.left = True
                if event.key == pygame.K_RIGHT:
                    self.right = True
                if event.key == pygame.K_ESCAPE:
                    self.running = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.left = False
                if event.key == pygame.K_RIGHT:
                    self.right = False
        if self.left and self.right:
            self.left = self.right = False
    
if __name__ == "__main__":
    main()   
        
                        

                            
