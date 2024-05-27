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
    CAR = scale_image(pygame.image.load("C:/Users/zbyta/OneDrive/Pulpit/ReinforcmentTraningInAGame/game/images/car.png"), 1.8)

    return {
        "GRASS": GRASS,
        "TRACK": TRACK,
        "TRACK_BORDER": TRACK_BORDER,
        "TRACK_BORDER_MASK": TRACK_BORDER_MASK,
        "FINISH": FINISH,
        "FINISH_MASK": FINISH_MASK,
        "FINISH_POSITION": FINISH_POSITION,
        "CAR": CAR
    }
