import pygame

def load_fonts():
    FONT_LG = pygame.font.SysFont("Arial", 40, True)
    FONT_MD = pygame.font.SysFont("Arial", 26)
    FONT_SM = pygame.font.SysFont("Arial", 18)
    FONT_XL = pygame.font.SysFont("Arial", 60, True)
    return FONT_LG, FONT_MD, FONT_SM, FONT_XL
