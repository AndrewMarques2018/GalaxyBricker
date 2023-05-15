import os
from turtle import delay

from scripts.characters.Ball import Ball, BallType
from scripts.characters.Platform import Platform, PlatformType
from scripts.utils.Vector import Vector
from scripts.utils.Window import Window
from scripts.utils.Dimension import Dimension

import pygame


class GameEngine:
    def __init__(self):
        self.ball = None
        self.platform = None
        self.pygame = pygame
        self.pygame.init()
        self.windows = Window(pygame, "Galaxy Bricker", Dimension(780, 600))

    def run(self):
        self.platform = create_platform()
        self.ball = create_ball()
        self.windows.add_element(self.platform, self.ball)

        game_is_active = True
        while game_is_active:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    game_is_active = False

            update(self.platform, self.windows)
            update(self.ball, self.windows)
            self.windows.update()

        pygame.quit()


def update(element, windows):
    if (element.position.x + element.dimension.width) >= windows.dimension.width:
        element.speed.x *= -1
    elif element.position.x < 0:
        element.speed.x *= -1

    if (element.position.y + element.dimension.height) >= windows.dimension.height:
        element.speed.y *= -1
    elif element.position.y < 0:
        element.speed.y *= -1


def create_platform():
    platform = Platform(Vector(0, 500), Dimension(100, 15))
    platform.select_platform(PlatformType.animate2)
    platform.set_speed(0.5, 0.0)

    return platform


def create_ball():
    ball = Ball(Vector(0, 0), Dimension(20, 20))
    ball.select_ball(BallType.basic_white)
    ball.set_speed(1, 0.5)

    return ball
