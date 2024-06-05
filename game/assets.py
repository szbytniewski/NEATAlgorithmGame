import pygame
from utility import scale_image

def load_images():
    GRASS = scale_image(pygame.image.load("C:/Users/Zbyta/Desktop/Studia/semestr_4/ReinforcmentTraningInAGame/game/images/imgs/grass.jpg"), 2.5)
    TRACK = scale_image(pygame.image.load("C:/Users/Zbyta/Desktop/Studia/semestr_4/ReinforcmentTraningInAGame/game/images/imgs/track.png"), 0.9)
    TRACK_BORDER = scale_image(pygame.image.load("C:/Users/Zbyta/Desktop/Studia/semestr_4/ReinforcmentTraningInAGame/game/images/imgs/track-border.png"), 0.9)
    TRACK_BORDER_MASK = pygame.mask.from_surface(TRACK_BORDER)
    FINISH = pygame.image.load("C:/Users/Zbyta/Desktop/Studia/semestr_4/ReinforcmentTraningInAGame/game/images/imgs/finish.png")
    FINISH_MASK = pygame.mask.from_surface(FINISH)
    FINISH_POSITION = (130, 250)
    CAR = scale_image(pygame.image.load("C:/Users/Zbyta/Desktop/Studia/semestr_4/ReinforcmentTraningInAGame/game/images/car.png"), 1)
    CAR2 = scale_image(pygame.image.load("C:/Users/Zbyta/Desktop/Studia/semestr_4/ReinforcmentTraningInAGame/game/images/car2.png"), 0.8)
    EXIT_BUTTON = scale_image(pygame.image.load("C:/Users/Zbyta/Desktop/Studia/semestr_4/ReinforcmentTraningInAGame/game/images//Exit_Button.png"), 2)
    SELECT_BUTTON = scale_image(pygame.image.load("C:/Users/Zbyta/Desktop/Studia/semestr_4/ReinforcmentTraningInAGame/game/images/Select_Button.png"), 1)
    START_BUTTON = scale_image(pygame.image.load("C:/Users/Zbyta/Desktop/Studia/semestr_4/ReinforcmentTraningInAGame/game/images/Start_Button.png"), 2)
    BOSS = scale_image(pygame.image.load("C:/Users/Zbyta/Desktop/Studia/semestr_4/ReinforcmentTraningInAGame/game/images/final_boss.jpg"), 0.9)
    NOOB = scale_image(pygame.image.load("C:/Users/Zbyta/Desktop/Studia/semestr_4/ReinforcmentTraningInAGame/game/images/lvl1_Noob.jpg"), 0.3)

    return {
        "GRASS": GRASS,
        "TRACK": TRACK,
        "TRACK_BORDER": TRACK_BORDER,
        "TRACK_BORDER_MASK": TRACK_BORDER_MASK,
        "FINISH": FINISH,
        "FINISH_MASK": FINISH_MASK,
        "FINISH_POSITION": FINISH_POSITION,
        "CAR": CAR,
        "CAR2": CAR2,
        "EXIT": EXIT_BUTTON,
        "SELECT": SELECT_BUTTON,
        "START": START_BUTTON,
        "BOSS": BOSS,
        "NOOB": NOOB
    }
