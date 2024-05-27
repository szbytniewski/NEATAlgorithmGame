import pygame
import neat
import time
import os
import pickle
from car import ComputerCar
from assets import load_images

# Load images
images = load_images()
CAR_IMG = images["CAR"]
TRACK_BORDER_MASK = images["TRACK_BORDER_MASK"]
FINISH_MASK = images["FINISH_MASK"]
FINISH_POSITION = images["FINISH_POSITION"]

WIN_WIDTH, WIN_HEIGHT = images["TRACK"].get_width(), images["TRACK"].get_height()
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("AI Car Racing")

def draw_window(win, cars, images):
    for img, pos in images:
        win.blit(img, pos)
    for car in cars:
        car.draw(win)
    pygame.display.update()

def eval_genomes(genomes, config):
    win = WIN
    clock = pygame.time.Clock()
    cars = []
    nets = []
    ge = []

    for genome_id, genome in genomes:
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        cars.append(ComputerCar(4, 4, CAR_IMG))
        genome.fitness = 0
        ge.append(genome)

    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

        for i, car in enumerate(cars):
            output = nets[i].activate(car.get_data())
            choice = output.index(max(output))

            if choice == 0:
                car.rotate(left=True)
            elif choice == 1:
                car.rotate(right=True)

            car.move_forward()

            if car.collide(TRACK_BORDER_MASK) is not None:
                ge[i].fitness -= 50
                cars.pop(i)
                nets.pop(i)
                ge.pop(i)
                continue

            if car.collide(FINISH_MASK, *FINISH_POSITION) is not None:
                ge[i].fitness += 3000
                car.reset(car.START_POS)

            ge[i].fitness += car.vel

        if not cars:
            run = False
            break

        draw_window(win, cars, [(images["GRASS"], (0, 0)), (images["TRACK"], (0, 0)), (images["FINISH"], FINISH_POSITION), (images["TRACK_BORDER"], (0, 0))])

def run(config_file):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, config_file)
    p = neat.Population(config)

    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(10))

    winner = p.run(eval_genomes, 50)
    with open("best.pkl", "wb") as f:
        pickle.dump(winner, f)

if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config.txt")
    run(config_path)
