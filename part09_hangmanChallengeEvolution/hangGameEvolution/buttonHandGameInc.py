import pygame, sys, random, math
from typing import List
from utileInc import get_random_word, sanitize_word
from fontsInc import load_fonts

FONT_LG, FONT_MD, FONT_SM, FONT_XL = load_fonts()
from configInc import (
    WIDTH,
    HEIGHT,
)


class Button:
    def __init__(
        self, rect: pygame.Rect, label: str, font, bg=(230, 230, 230), fg=(0, 0, 0)
    ):
        self.rect = rect
        self.label = label
        self.font = font
        self.bg = bg
        self.fg = fg
        self.hover = False
        self.disabled = False

    def draw(self, surf):
        color = self.bg
        if self.disabled:
            color = (210, 210, 210)
        elif self.hover:
            color = tuple(min(255, c + 20) for c in color)
        pygame.draw.rect(surf, color, self.rect, border_radius=8)
        txt = self.font.render(
            self.label, True, self.fg if not self.disabled else (130, 130, 130)
        )
        txtr = txt.get_rect(center=self.rect.center)
        surf.blit(txt, txtr)

    def handle_event(self, ev):
        if ev.type == pygame.MOUSEMOTION:
            self.hover = self.rect.collidepoint(ev.pos)
        if self.disabled:
            return False
        if (
            ev.type == pygame.MOUSEBUTTONDOWN
            and ev.button == 1
            and self.rect.collidepoint(ev.pos)
        ):
            return True
        return False


def draw_scores_panel(self, surf):
    panel_w, panel_h = 400, 320
    panel_rect = pygame.Rect(
        (WIDTH - panel_w) // 2, (HEIGHT - panel_h) // 2, panel_w, panel_h
    )
    pygame.draw.rect(surf, (240, 240, 240), panel_rect, border_radius=16)
    pygame.draw.rect(surf, (180, 180, 180), panel_rect, 3, border_radius=16)

    self.btn_close_scores = Button(
        pygame.Rect(panel_rect.right - 40, panel_rect.top + 10, 30, 30),
        "X",
        FONT_SM,
        bg=(200, 80, 80),
        fg=(255, 255, 255),
    )
    self.btn_close_scores.draw(surf)

    # titre
    title = FONT_MD.render("Meilleurs Joueurs", True, (0, 0, 0))
    title_rect = title.get_rect(center=(panel_rect.centerx, panel_rect.top + 50))
    surf.blit(title, title_rect)

    # top 5
    top5 = self.hs.get_top(5)
    y = title_rect.bottom + 20
    for i, row in enumerate(top5):
        line = f"{i+1}. {row['name']} — {row['score']} pts"
        txt = FONT_SM.render(line, True, (50, 50, 50))
        txt_rect = txt.get_rect(center=(panel_rect.centerx, y))
        surf.blit(txt, txt_rect)
        y += 30

    if not top5:
        msg = FONT_SM.render("Aucun score enregistré", True, (120, 120, 120))
        msg_rect = msg.get_rect(center=panel_rect.center)
        surf.blit(msg, msg_rect)
