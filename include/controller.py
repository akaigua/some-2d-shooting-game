import pygame


def check_event():
    left, right, up, attack, leave = [False] * 6

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            leave = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                leave = True
            if event.key == pygame.K_a:
                left = True
            if event.key == pygame.K_d:
                right = True
            if event.key == pygame.K_SPACE:
                up = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                leave = False
            if event.key == pygame.K_a:
                left = False
            if event.key == pygame.K_d:
                right = False
            if event.key == pygame.K_SPACE:
                up = False

    return [left, right, up, attack, leave]