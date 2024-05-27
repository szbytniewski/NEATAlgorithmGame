import math
import time
import pygame
from utility import blit_rotate_center
from assets import load_images
from car import PlayerCar

# Load images
images = load_images()
GRASS = images["GRASS"]
TRACK = images["TRACK"]
TRACK_BORDER = images["TRACK_BORDER"]
TRACK_BORDER_MASK = images["TRACK_BORDER_MASK"]
FINISH = images["FINISH"]
FINISH_MASK = images["FINISH_MASK"]
FINISH_POSITION = images["FINISH_POSITION"]
CAR = images["CAR"]

WIDTH, HEIGHT = TRACK.get_width(), TRACK.get_height()
WIN = pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption("Game")

FPS = 120

def draw(win, images, player_car):
    for img, pos in images:
        win.blit(img, pos)

    player_car.draw(win)
    pygame.display.update()


def move_player(player_car):
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

run=True
clock = pygame.time.Clock()
images = [(GRASS, (0, 0)), (TRACK, (0, 0)),
          (FINISH, FINISH_POSITION), (TRACK_BORDER, (0, 0))]
player_car = PlayerCar(4, 4, CAR)
while run:
    clock.tick(FPS)

    draw(WIN, images, player_car)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

    move_player(player_car)

    if player_car.collide(TRACK_BORDER_MASK) != None:
        player_car.bounce()

    finish_poi_collide = player_car.collide(FINISH_MASK, *FINISH_POSITION)
    if finish_poi_collide != None:
        if finish_poi_collide[1] == 0:
            player_car.bounce()
        else:
            player_car.reset()
            print("finish")


pygame.quit()