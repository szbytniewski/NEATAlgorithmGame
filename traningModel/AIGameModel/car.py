import math
import pygame
from utility import blit_rotate_center

class Car:
    def __init__(self, max_vel, rotation_vel, img, start_pos):
        self.img = img
        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = 0
        self.x, self.y = start_pos
        self.acceleration = 0.08

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
        self.vel = max(self.vel - self.acceleration, -self.max_vel / 2)
        self.move()

    def move(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel
        self.y -= vertical
        self.x -= horizontal

    def collide(self, mask, x=0, y=0):
        car_mask = pygame.mask.from_surface(self.img)
        offset = (int(self.x - x), int(self.y - y))
        poi = mask.overlap(car_mask, offset)
        return poi

    def reset(self, start_pos):
        self.x, self.y = start_pos
        self.angle = 0
        self.vel = 0

class ComputerCar(Car):
    START_POS = (180, 200)

    def __init__(self, max_vel, rotation_vel, img):
        super().__init__(max_vel, rotation_vel, img, self.START_POS)

    def reduce_speed(self):
        self.vel = max(self.vel - self.acceleration / 2, 0)
        self.move()

    def bounce(self):
        self.vel = -self.vel + (self.vel / 2)
        self.move()

    def get_data(self):
        # Example data to collect
        return [
            self.vel,
            self.angle,
            self.get_distance_to_border('left'),
            self.get_distance_to_border('right'),
            self.get_distance_to_finish()
        ]

    def get_distance_to_border(self, direction):
        left_border_position = (0, self.y)
        right_border_position = (100, self.y)

        if direction == 'left':
            border_position = left_border_position
        elif direction == 'right':
            border_position = right_border_position

        x_car, y_car = self.x, self.y
        x_border, y_border = border_position
        distance = math.sqrt((x_border - x_car) ** 2 + (y_border - y_car) ** 2)
        return distance

    def get_distance_to_finish(self):
        x_car, y_car = self.x, self.y
        x_finish, y_finish = 130, 250
        distance = math.sqrt((x_finish - x_car) ** 2 + (y_finish - y_car) ** 2)
        return distance
