#! /usr/bin/env python3
''' Starter code for HW3, problem 1 '''
import pygame

TEXT = '''When designing a game, it is very important to provide help to the player.
Help in a game is often given by writing long instructions on the screen.
There may be better methods, however!'''

def main():
    pygame.init()
    window_size_x = 1200
    window_size_y = 622
    surface = pygame.display.set_mode([window_size_x,window_size_y]) 
    pygame.display.set_caption('Mario as a Sprite')
    background = pygame.image.load('mario_background.png').convert()
    surface.blit(background, (0,0))
    
    fontobj = setup_fonts(18)
    wrapped_rect = pygame.Rect(100, 30, 210, 500)
    wrapped_surface = word_wrap(wrapped_rect, fontobj, (200, 0, 0), TEXT)
            
    while True:
        quit, click, click2 = check_events()
        if quit:
            break
        if click:
            wrapped_rect.center = click
            
        surface.blit(background, (0,0))
        surface.blit(wrapped_surface, wrapped_rect)
        pygame.draw.rect(surface, (0,0,0), wrapped_rect, width=1)
        pygame.display.flip()

def word_wrap(rect, font, color, text):
    ''' Wrap the text into the space of the rect, using the font object provided.
        Returns a surface of rect size with the text rendered in it.
    '''
    '''
    wrapped_rect = pygame.Rect(100, 30, 210, 500)
    rect_size_x = 210
    width, height = pygame.font.Font.size(text)
    line = ' ' * rect_size_x
    f = 0
    for i in text:
        if i > (rect_size_x * f) / width:
            pygame.font.render(text[(i * (f - 1)) : (i * f)], True, color, background = None)
            linesize = pygame.font.Font.get_linesize(font)
            #pygame.font.render(line, True, color, background = None)
            wrapped_rect.topleft = (100, 30 + f * (setup_fonts.font_size + linesize))
            f += 1
    '''       
    return pygame.font.render(text, True, color, background = None)
    #return pygame.font.Font.size(text)

    
    
def setup_fonts(font_size, bold=False, italic=False):
    ''' Load a font, given a list of preferences

        The preference list is a sorted list of strings (should probably be a parameter),
        provided in a form from the FontBook list. 
        Any available font that starts with the same letters (lowercased, spaces removed) 
        as a font in the font_preferences list will be loaded.
        If no font can be found from the preferences list, the pygame default will be returned.

        returns -- A Font object
    '''
    font_preferences = ['Helvetica Neue', 'Iosevka Regular', 'Comic Sans', 'Courier New']
    available = pygame.font.get_fonts()
    prefs = [x.lower().replace(' ', '') for x in font_preferences]
    for pref in prefs:
        a = [x
             for x in available
             if x.startswith(pref)
            ]
        if a:
            fonts = ','.join(a) #SysFont expects a string with font names in it
            return pygame.font.Font.SysFont(fonts, font_size, bold, italic)
    return pygame.font.SysFont(None, font_size, bold, italic)
    
def check_events():
    ''' A controller of sorts.  Looks for Quit, several simple events.
        Returns: True/False for if a Quit event happened.
    '''
    
    quit = False
    click = click2 = None
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                quit = True
            if event.key == pygame.K_ESCAPE:
                quit = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                click = event.pos
            if event.button == 3:
                click2 = event.pos
                
    return quit, click, click2

if __name__ == "__main__":
    main()