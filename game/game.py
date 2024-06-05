import math
import time
import pygame
import neat
import os
import pickle
from utility import blit_rotate_center
from assets import load_images
from car import PlayerCar, ComputerCar

pygame.init()

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
CAR2 = images["CAR2"]
EXIT_BUTTON = images["EXIT"]
SELECT_BUTTON = images["SELECT"]
START_BUTTON = images["START"]
BOSS = images["BOSS"]
NOOB = images["NOOB"]

WIDTH, HEIGHT = TRACK.get_width(), TRACK.get_height()
WIN = pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption("Game")

FPS = 60
MAIN_FONT = pygame.font.SysFont("comicsans", 26)

def draw(win, images, cars, curr_lap):
    for img, pos in images:
        win.blit(img, pos)

    for car in cars:
        car.draw(win)

    lap_text = MAIN_FONT.render(f"Laps: {curr_lap}/3", 1, (255, 255, 255))
    win.blit(lap_text, (10, HEIGHT - 45))

    pygame.display.update()

def draw_winner(win, winner):
    font = pygame.font.SysFont("comicsans", 64)
    text = font.render(f"{winner} Wins!", True, (114, 66, 245))
    win.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
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

def menu():
    run = True
    selection_phase = False

    while run:
        WIN.fill((0, 0, 0))

        if not selection_phase:
            # Initial menu with game title, start, and exit buttons
            title_font = pygame.font.SysFont("comicsans", 60)
            title_label = title_font.render("RACING GAME", 1, (255, 255, 255))
            WIN.blit(title_label, (WIDTH//2 - title_label.get_width()//2, HEIGHT//4))

            WIN.blit(images["START"], (WIDTH//2 - images["START"].get_width()//2, HEIGHT//2))
            WIN.blit(images["EXIT"], (WIDTH//2 - images["EXIT"].get_width()//2, HEIGHT//2 + images["START"].get_height() + 10))
        
        else:
            # Selection phase with car choices
            select_font = pygame.font.SysFont("comicsans", 44)
            select_label = select_font.render("Select the driver you want to race with:", 1, (255, 255, 255))
            WIN.blit(select_label, (WIDTH//2 - select_label.get_width()//2, HEIGHT//4))

            WIN.blit(images["BOSS"], (WIDTH//4 - images["BOSS"].get_width()//2, HEIGHT//2))
            WIN.blit(images["NOOB"], (3*WIDTH//4 - images["NOOB"].get_width()//2, HEIGHT//2))
        
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                
                if not selection_phase:
                    # Check for Start and Exit button clicks
                    if WIDTH//2 - images["START"].get_width()//2 < mouse_pos[0] < WIDTH//2 + images["START"].get_width()//2 and HEIGHT//2 < mouse_pos[1] < HEIGHT//2 + images["START"].get_height():
                        selection_phase = True
                    if WIDTH//2 - images["EXIT"].get_width()//2 < mouse_pos[0] < WIDTH//2 + images["EXIT"].get_width()//2 and HEIGHT//2 + images["START"].get_height() + 10 < mouse_pos[1] < HEIGHT//2 + images["START"].get_height() + 10 + images["EXIT"].get_height():
                        pygame.quit()
                        quit()
                
                else:
                    # Check for car selection clicks
                    if WIDTH//4 - images["BOSS"].get_width()//2 < mouse_pos[0] < WIDTH//4 + images["BOSS"].get_width()//2 and HEIGHT//2 < mouse_pos[1] < HEIGHT//2 + images["BOSS"].get_height():
                        return "C:/Users/Zbyta/Desktop/Studia/semestr_4/ReinforcmentTraningInAGame/Models/best.pkl"
                    if 3*WIDTH//4 - images["NOOB"].get_width()//2 < mouse_pos[0] < 3*WIDTH//4 + images["NOOB"].get_width()//2 and HEIGHT//2 < mouse_pos[1] < HEIGHT//2 + images["NOOB"].get_height():
                        return "C:/Users/Zbyta/Desktop/Studia/semestr_4/ReinforcmentTraningInAGame/Models/worst.pkl"
    
    return None



def main():
    clock = pygame.time.Clock()
    images_to_draw = [(GRASS, (0, 0)), (TRACK, (0, 0)), (FINISH, FINISH_POSITION), (TRACK_BORDER, (0, 0))]
    player_car = PlayerCar(4, 4, CAR2, WIDTH, HEIGHT, TRACK_BORDER_MASK)

    model_filename = menu()
    if not model_filename:
        return

    with open(model_filename, "rb") as f:
        best_genome = pickle.load(f)

    config_path = "C:/Users/Zbyta/Desktop/Studia/semestr_4/ReinforcmentTraningInAGame/AIGameModel/config.txt"
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)
    best_model = neat.nn.FeedForwardNetwork.create(best_genome, config)

    computer_car = ComputerCar(4, 4, CAR, WIDTH, HEIGHT, TRACK_BORDER_MASK, best_model)

    player_laps = 0
    computer_laps = 0
    run = True
    while run:
        clock.tick(FPS)

        draw(WIN, images_to_draw, [player_car, computer_car], player_laps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        move_player(player_car)
        computer_car.update()

        if player_car.collide(TRACK_BORDER_MASK) != None:
            player_car.bounce()

        if computer_car.collide(TRACK_BORDER_MASK) != None:
            computer_car.bounce()

        # The info what happends after someone crosses the finish line (NEEDS UPDATE)
        finish_poi_collide = player_car.collide(FINISH_MASK, *FINISH_POSITION)
        if finish_poi_collide != None:
            if finish_poi_collide[1] == 0:
                player_car.bounce()
            else:
                player_car.reset(player_car.START_POS)
                player_laps += 1
                if player_laps == 3:
                    run = False

        finish_poi_collide = computer_car.collide(FINISH_MASK, *FINISH_POSITION)
        if finish_poi_collide is not None:
            if finish_poi_collide[1] == 0:
                computer_car.bounce()
            else:
                computer_car.reset(computer_car.START_POS)
                computer_laps += 1
                if computer_laps == 3:
                    run = False

        if player_laps == 3:
            winner = "Player"
            run = False
        elif computer_laps == 3:
            winner = "Computer"
            run = False

    if winner:
        draw_winner(WIN, winner)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                pygame.quit()
                return

if __name__ == "__main__":
    main()