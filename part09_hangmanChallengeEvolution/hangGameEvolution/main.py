"""
Hangman — Pygame
"""

import pygame, sys, random, math
from typing import List
from configInc import WIDTH, HEIGHT, FPS, BG_COLOR, LEFT_PANEL_W
from utileInc import get_random_word, sanitize_word

pygame.init()
from fontsInc import load_fonts

FONT_LG, FONT_MD, FONT_SM, FONT_XL = load_fonts()
from handGameInc import HangmanGame

pygame.display.set_caption("Jeu du Pendu — Pygame")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


def main():
    game = HangmanGame()
    game.start_new()

    running = True
    while running:
        dt = clock.tick(FPS) / 1000.0
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                running = False
            else:
                game.handle_event(ev)

        game.update(dt)

        # draw
        screen.fill(BG_COLOR)
        # left panel + right
        # left panel background rounded will be drawn by game.draw_left_panel
        game.draw_left_panel(screen)
        game.draw_right_panel(screen)
        game.draw_keyboard(screen)

        footer = FONT_SM.render(
            "Échap: Quitter | Enter: Proposer un mot complet | Clique touches ou clavier",
            True,
            (100, 100, 100),
        )
        screen.blit(footer, (LEFT_PANEL_W + 24, HEIGHT - 28))

        pygame.display.flip()

    pygame.quit()
    sys.exit()


main()
