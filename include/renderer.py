import pygame

pygame.init()

def render(surface,n: dict,d:dict):
    # The n(ew),d(elete) dict should be looked like: {(tuple contain the coordinate of character) : the asset name
    # that needs to be rendered as a string}
    for key, value in n:
        assert type(key) == tuple and len(key) == 2 and type(key[0]) == int and type(key[1]) == int, \
            "The coordinate must be in a tuple that looks like (x,y) where x,y is both int"

