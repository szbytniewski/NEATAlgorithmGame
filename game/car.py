import math
import pygame
import neat
from utility import blit_rotate_center

class Car:
    def __init__(self, max_vel, rotation_vel, img, start_pos, win_width, win_height, track_border_mask):
        self.img = img
        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = 0
        self.x, self.y = start_pos
        self.acceleration = 0.08
        self.win_width = win_width
        self.win_height = win_height
        self.track_border_mask = track_border_mask
        self.sensor_length = 100

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
        self.vel = self.vel // 2

    def get_data(self):
        sensors = self.get_sensor_data()
        return [
            self.vel,
            self.angle,
            sensors[0],
            sensors[1],
            sensors[2],
            sensors[3],
            sensors[4]
        ]

    def get_sensor_data(self):
        # [front, left-front, left, right-front, right] sensors pointing
        sensor_angles = [90, 45, 0, 135, 180]
        distances = []

        for angle in sensor_angles:
            distances.append(self.cast_ray(angle))

        return distances

    def cast_ray(self, angle):
        length = 0

        # Starting point for the rays to cast from (middle of the car image)
        x = int(self.x + self.img.get_width() // 2)
        y = int(self.y + self.img.get_height() // 2)

        while length < 100:  # Maximum sensor range
            length += 1
            end_x = int(x + math.cos(math.radians(self.angle + angle)) * length)
            end_y = int(y - math.sin(math.radians(self.angle + angle)) * length)
            if 0 <= end_x < self.win_width and 0 <= end_y < self.win_height:
                if self.track_border_mask.get_at((end_x, end_y)):
                    break
            else:
                break
        return length



class PlayerCar(Car):
    START_POS = (160, 200)

    def __init__(self, max_vel, rotation_vel, img, win_width, win_height, track_border_mask):
        super().__init__(max_vel, rotation_vel, img, self.START_POS, win_width, win_height, track_border_mask)

    def reduce_speed(self):
        self.vel = max(self.vel - self.acceleration / 2, 0)
        self.move()

    def bounce(self):
        self.vel = -self.vel + (self.vel / 2)
        self.move()

class ComputerCar(Car):
    START_POS = (180, 200)

    def __init__(self, max_vel, rotation_vel, img, win_width, win_height, track_border_mask, model):
        super().__init__(max_vel, rotation_vel, img, self.START_POS, win_width, win_height, track_border_mask)
        self.model = model

    def update(self):
        data = self.get_data()
        output = self.model.activate(data)
        choice = output.index(max(output))

        if choice == 0:
            self.rotate(left=True)
        elif choice == 1:
            self.rotate(right=True)

        self.move_forward()

    def reduce_speed(self):
        self.vel = max(self.vel - self.acceleration / 2, 0)
        self.move()

    def bounce(self):
        self.vel = -self.vel + (self.vel / 2)
        self.move()