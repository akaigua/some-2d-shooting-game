import pygame


def render(r: dict):
    # The r dict should be looked like: {(tuple contain the coordinate of character) : the asset name that needs to be
    # rendered as a string}
    for key, value in r:
        assert type(key) == tuple, "The coordinate must be in a tuple that looks like (x,y)"
