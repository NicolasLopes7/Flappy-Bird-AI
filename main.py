import pygame
import neat
import time
import os
import random

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 800


def loadimage(fileName):
    return pygame.transform.scale2x(pygame.image.load(os.path.join("assets", fileName)))


BIRD_IMGS = [
    loadImage("bird1.png"),
    loadImage("bird2.png"),
    loadImage("bird3.png")]

PIPE_IMG = loadImage("pipe.png")
BASE_IMG = loadImage("base.png")
BG_IMG = loadImage("bg.png")


class Bird:
    IMGS = BIRD_IMGS
    MAX_ROTATION = 25
    ROT_VEL = 20
    ANIMATION_TIME = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt = 0
        self.tick_count = 0
        self.vel = 0
        self.height = self.y
        self.img_count = 0
        self.img = self.IMGS[0]
