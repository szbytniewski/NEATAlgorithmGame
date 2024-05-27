import math
import time

import pygame
from imgUtil import blit_rotate_center, scale_image

GRASS = scale_image(pygame.image.load("C:/Users/zbyta/OneDrive/Pulpit/ReinforcmentTraningInAGame/game/images/Grass.png"), 3)
TRACK = scale_image(pygame.image.load("C:/Users/zbyta/OneDrive/Pulpit/ReinforcmentTraningInAGame/game/images/Track.png"), 2)

TRACK_BORDER = scale_image(pygame.image.load("C:/Users/zbyta/OneDrive/Pulpit/ReinforcmentTraningInAGame/game/images/outLine.png"), 2)

CAR = scale_image(pygame.image.load("C:/Users/zbyta/OneDrive/Pulpit/ReinforcmentTraningInAGame/game/images/car.png"), 1.5)

WIDTH, HEIGHT = TRACK.get_width(), TRACK.get_height()
WIN = pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption("Game")

FPS = 120

class Car:
    def __init__(self, max_vel, rotation_vel):
        self.img = self.IMG
        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = 0
        self.x, self.y = self.START_POS
        self.acceleration = 0.1

    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel

    def draw(self, win):
        blit_rotate_center(win, self.img, (self.x, self.y), self.angle)

    def move_forward(self):
        self.vel = min(self.vel + self.acceleration, self.max_vel)
        self.move()

    def move_backward(self):
        self.vel = max(self.vel - self.acceleration, -self.max_vel/3)
        self.move()

    def move(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel

        self.y -= vertical
        self.x -= horizontal


class PlayerCar(Car):
    IMG = CAR
    START_POS = (200,200)
    
    def reduce_speed(self):
        self.vel = max(self.vel - self.acceleration / 2, 0)
        self.move()


def draw(win, images, player_car):
    for img, pos in images:
        win.blit(img, pos)

    player_car.draw(win)
    pygame.display.update()

run=True
clock = pygame.time.Clock()
images = [(GRASS,(0,0)), (TRACK,(0,0)), (CAR, (0,0))]
player_car = PlayerCar(8, 6)
while run:
    clock.tick(FPS)

    draw(WIN, images, player_car)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

    keys = pygame.key.get_pressed()
    moved = False

    if keys[pygame.K_a]:
        player_car.rotate(left=True)
    if keys[pygame.K_d]:
        player_car.rotate(right=True)
    if keys[pygame.K_w]:
        moved = True
        player_car.move_forward()
    if keys[pygame.K_s]:
        moved = True
        player_car.move_backward()

    if not moved:
        player_car.reduce_speed()

pygame.quit()