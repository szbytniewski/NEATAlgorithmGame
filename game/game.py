import math
import time

import pygame

from game.imgUtil import blit_rotate_center, scale_image

GRASS = scale_image(pygame.image.load("C:/Users/zbyta/OneDrive/Pulpit/ReinforcmentTraningInAGame/game/images/Grass.png"), 2.9)

WIDTH, HEIGHT = GRASS.get_width(), GRASS.get_height()
WIN = pygame.display.set_mode([1040,520])
pygame.display.set_caption("Game")

CAR = 5

class Car:
    IMG = CAR

    def __init__(self, max_vel, rotation_vel):
        self.image = self.IMG
        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = 0

    def rotate(self, turnRight=False, turnLeft=False):
        if(turnLeft):
            self.angle += self.rotation_vel
        elif(turnRight):
            self.angle -= self.rotation_vel

    def draw(self, win):
        # blit_rotate_center(win, self.image, )
        pass

def draw(win, images):
    for image, pos in images:
        win.blit(image, pos)

run=True
images = [(GRASS,(0,0))]
while run:

    draw(WIN, images)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

pygame.quit()