import pygame, sys, random, math
from typing import List

from buttonHandGameInc import Button
from utileInc import get_random_word, sanitize_word
from fontsInc import load_fonts
from highscoresInc import HighScoreManager
FONT_LG, FONT_MD, FONT_SM, FONT_XL = load_fonts()
from configInc import (WIDTH,HEIGHT,LEFT_PANEL_W,MARGIN,KEY_SIZE,KEY_MARGIN,MAX_PENALTIES,PANEL_COLOR,ACCENT,BAD,TEXT_COLOR,)

class HangmanGame:
    def __init__(self):
        self.reset_state()
        self.create_keyboard()
        self.info_message = "Appuie sur une lettre ou clique sur le clavier."
        self.anim_timer = 0.0

        self.hs = HighScoreManager("highscores.json", top_n=10)
        self.show_scores = False
        self.btn_scores = None
        self.btn_close_scores = None

    def compute_score(self) -> int:
        score_base = 1000
        score = (score_base - self.penalties * 150 - self.attempts * 5 + self.revealed_count * 10)
        return max(0, score)

    def reset_state(self):
        self.secret = ""
        self.display = ""
        self.proposed_letters: List[str] = []
        self.proposed_words: List[str] = []
        self.penalties = 0
        self.attempts = 0
        self.won = False
        self.lost = False
        self.revealed_count = 0

    def start_new(self, word: str = None):
        self.reset_state()
        if word:
            chosen = sanitize_word(word)
            if not chosen:
                chosen = get_random_word()
        else:
            chosen = get_random_word()
        self.secret = sanitize_word(chosen)
        self.display = "_" * len(self.secret)
        self.info_message = "Nouveau mot choisi."
        self.anim_timer = 0

    def create_keyboard(self):
        # Create buttons A-Z placed in grid
        self.keys = []
        letters = [chr(ord("A") + i) for i in range(26)]
        cols = 10
        x0 = LEFT_PANEL_W + MARGIN
        y0 = HEIGHT - 200
        w = KEY_SIZE
        h = KEY_SIZE
        for i, L in enumerate(letters):
            col = i % cols
            row = i // cols
            x = x0 + col * (w + KEY_MARGIN)
            y = y0 + row * (h + KEY_MARGIN)
            rect = pygame.Rect(x, y, w, h)
            btn = Button(rect, L, FONT_SM, bg=(240, 240, 240), fg=TEXT_COLOR)
            self.keys.append(btn)

    def propose_letter(self, ch: str):
        ch = ch.lower()
        if self.won or self.lost:
            return
        if not ch.isalpha() or len(ch) != 1:
            return
        if ch in self.proposed_letters:
            self.info_message = f"Lettre '{ch}' déjà proposée."
            return
        self.proposed_letters.append(ch)
        self.attempts += 1
        if ch in self.secret:
            # reveal all occurrences
            new_display = list(self.display)
            good = 0
            for i, c in enumerate(self.secret):
                if c == ch and new_display[i] == "_":
                    new_display[i] = ch
                    good += 1
            self.display = "".join(new_display)
            self.revealed_count += good
            self.info_message = f"Bien joué ! '{ch}' est dans le mot."
        else:
            self.penalties += 1
            self.info_message = f"Raté ! '{ch}' n'est pas dans le mot. ({self.penalties}/{MAX_PENALTIES})"
        self.check_end()

    def propose_word(self, w: str):
        if self.won or self.lost:
            return
        w = sanitize_word(w)
        if not w:
            return
        if w in self.proposed_words:
            self.info_message = "Mot déjà proposé."
            return
        self.proposed_words.append(w)
        self.attempts += 1
        if w == self.secret:
            self.display = self.secret
            self.won = True
            self.info_message = f"Bravo ! Mot trouvé : {self.secret}"
        else:
            # heavy penalty for wrong full-word guess
            self.penalties += 3
            self.info_message = (f"Mauvais mot — pénalité +3 ({self.penalties}/{MAX_PENALTIES})")
        self.check_end()

    def check_end(self):
        if "_" not in self.display:
            self.won = True
            final_score = self.compute_score()
            if self.hs.qualifies(final_score):
                self.info_message = f"Tu as gagné en {self.attempts} essais!"
                self.msg_won_game = f"Ton score: {final_score} pts. Tu a batu le record !"

                pygame.display.iconify()
                name = input(f"Bravo ! Score: {final_score}. Entre ton nom : ").strip()[:20]
                if not name:
                    name = "Anonyme"
                self.hs.insert(name, final_score, self.attempts, self.penalties)
                print("Score enregistré.")
                pygame.display.set_mode((WIDTH, HEIGHT))
            else:
                self.info_message = f"Tu as gagné en {self.attempts} essais !"
                self.msg_won_game = f"Ton score: {final_score} pts. Le meilleur score actuel est de {self.hs.get_top(1)[0]['score']} detenu par {self.hs.get_top(1)[0]['name']}."
        if self.penalties >= MAX_PENALTIES:
            self.lost = True
            self.info_message = f"Perdu ! le mot était : {self.secret}"

    def draw_left_panel(self, surf):
        # panel background
        panel = pygame.Rect(
            MARGIN, MARGIN, LEFT_PANEL_W - 2 * MARGIN, HEIGHT - 2 * MARGIN
        )
        pygame.draw.rect(surf, PANEL_COLOR, panel, border_radius=12)

        # title
        title = FONT_LG.render("Jeu du Pendu", True, TEXT_COLOR)
        surf.blit(title, (panel.x + 18, panel.y + 18))

        # secret display (spaced)
        spaced = " ".join(self.display.upper())
        secret_surf = FONT_XL.render(spaced, True, TEXT_COLOR)
        secret_rect = secret_surf.get_rect(
            center=(panel.x + panel.w // 2, panel.y + 140)
        )
        surf.blit(secret_surf, secret_rect)
        # Info message

        # Gestion automatique des retours à la ligne (\n)
        lines = self.info_message.split("\n")
        y = panel.y + 210  # position de départ verticale
        for line in lines:
            info_surf = FONT_MD.render(line, True, TEXT_COLOR)
            surf.blit(info_surf, (panel.x + 18, y))
            y += info_surf.get_height() + 2  # espace entre les lignes

        # Proposed letters
        pl = "Lettres: " + ", ".join(sorted(self.proposed_letters))
        surf_pl = FONT_SM.render(pl, True, (80, 80, 80))
        surf.blit(surf_pl, (panel.x + 18, panel.y + 260))

        # Attempts & penalties
        stats = (f"Essais: {self.attempts}    Pénalités: {self.penalties}/{MAX_PENALTIES}")
        surf_stats = FONT_SM.render(stats, True, (80, 80, 80))
        surf.blit(surf_stats, (panel.x + 18, panel.y + 300))

        # Buttons (New random / Enter custom)
        btn_w = 150
        btn_h = 42
        self.btn_new = Button(pygame.Rect(panel.x + 18, panel.y + 340, btn_w, btn_h),"Nouveau mot",FONT_SM,bg=ACCENT,fg=(255, 255, 255),)
        self.btn_custom = Button(pygame.Rect(panel.x + 18 + btn_w + 12, panel.y + 340, btn_w, btn_h),"Mot custom",FONT_SM,bg=(80, 80, 80),fg=(255, 255, 255),)
        self.btn_hint = Button(pygame.Rect(panel.x + 25, panel.y + 340 + btn_h + 12, btn_w * 2, btn_h),"Indice (révèle 1 & +1 pénalite)",FONT_SM,bg=(200, 200, 200),)
        self.btn_scores = Button(pygame.Rect(panel.x + 25, panel.y + 340 + btn_h * 2 + 24, btn_w * 2, btn_h),"Meilleurs scores",FONT_SM,bg=(150, 200, 250),fg=(0, 0, 0),)
        self.btn_new.draw(surf)
        self.btn_custom.draw(surf)
        self.btn_hint.draw(surf)
        self.btn_scores.draw(surf)

    def draw_right_panel(self, surf):
        # draw hangman on right area
        cx = LEFT_PANEL_W + (WIDTH - LEFT_PANEL_W) // 2
        cy = 220
        # platform / gallows
        base_x = LEFT_PANEL_W + 60
        # draw base
        pygame.draw.line(surf, (80, 80, 80), (base_x, 420), (base_x + 200, 420), 8)
        pygame.draw.line(surf, (80, 80, 80), (base_x + 30, 420), (base_x + 30, 100), 10)
        pygame.draw.line(surf, (80, 80, 80), (base_x + 30, 100), (base_x + 140, 100), 8)
        pygame.draw.line(surf, (80, 80, 80), (base_x + 140, 100), (base_x + 140, 140), 6)

        # draw progressive stickman depending on penalties
        step = self.penalties
        # head
        if step >= 1:
            pygame.draw.circle(
                surf, BAD if self.lost else ACCENT, (base_x + 140, 170), 28, 4
            )
        if step >= 2:
            pygame.draw.line(surf, ACCENT, (base_x + 140, 198), (base_x + 140, 300), 6)
        if step >= 3:
            pygame.draw.line(
                surf, ACCENT, (base_x + 140, 220), (base_x + 200, 260), 6
            )  # right arm
        if step >= 4:
            pygame.draw.line(
                surf, ACCENT, (base_x + 140, 220), (base_x + 80, 260), 6
            )  # left arm
        if step >= 5:
            pygame.draw.line(
                surf, ACCENT, (base_x + 140, 300), (base_x + 180, 360), 6
            )  # right leg
        if step >= 6:
            pygame.draw.line(
                surf, ACCENT, (base_x + 140, 300), (base_x + 100, 360), 6
            )  # left leg

        # subtle animation for correct guess
        if self.won:
            win_txt = FONT_XL.render("GAGNÉ !", True, ACCENT)
            surf.blit(win_txt, (LEFT_PANEL_W + 60, 30))
            msg_end_game = FONT_MD.render(self.msg_won_game, True, TEXT_COLOR)
            surf.blit(msg_end_game, (LEFT_PANEL_W + 60, 450))
        if self.lost:
            lose_txt = FONT_XL.render("PERDU", True, BAD)
            surf.blit(lose_txt, (LEFT_PANEL_W + 60, 30))
            reveal = FONT_MD.render(f"Mot : {self.secret}", True, TEXT_COLOR)
            surf.blit(reveal, (LEFT_PANEL_W + 60, 450))

    def draw_keyboard(self, surf):
        if self.show_scores:
            self.draw_scores_panel(surf)
        for btn in self.keys:
            # disable keys already used
            key_label = btn.label.lower()
            btn.disabled = (key_label in self.proposed_letters) or self.won or self.lost
            btn.draw(surf)

    def update(self, dt):
        self.anim_timer += dt
        # example of small animation usage: highlight a key after correct guess (not expanded)
        pass

    def handle_event(self, ev):
        if self.show_scores:
            if ev.type in (pygame.MOUSEMOTION, pygame.MOUSEBUTTONDOWN):
                if self.btn_close_scores and self.btn_close_scores.handle_event(ev):
                    self.show_scores = False
            return
        # keyboard input (letters + enter for full word)
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if self.won or self.lost:
                if ev.key == pygame.K_RETURN:
                    self.start_new()
                return
            if ev.key == pygame.K_RETURN:
                # cut prompt for full word - show simple console input (blocking) OR we can open a modal
                # For simplicity use blocking console input here (visible in terminal)
                pygame.key.set_repeat()  # stop repeats
                word = input("Proposez un mot complet : ").strip()
                self.propose_word(word)
            else:
                ch = ev.unicode
                if ch and ch.isalpha():
                    self.propose_letter(ch)
        # mouse events for UI buttons and on-screen keys
        if ev.type in (pygame.MOUSEMOTION, pygame.MOUSEBUTTONDOWN):
            # keyboard buttons
            for b in self.keys:
                if b.handle_event(ev):
                    # clicked a letter
                    self.propose_letter(b.label)
            # left panel buttons
            # detect clicks on the generated buttons
            if (hasattr(self, "btn_new") and hasattr(self, "btn_custom") and hasattr(self, "btn_hint") and hasattr(self, "btn_scores")):
                if self.btn_new.handle_event(ev):
                    self.start_new()
                if self.btn_custom.handle_event(ev):
                    # blocking console input for custom word entry (simple)
                    pygame.display.iconify()  # minimize window to allow terminal focus on some platforms
                    w = input("Joueur 1 — Entrez le mot secret (lettres uniquement) : ").strip()
                    pygame.display.set_mode((WIDTH, HEIGHT))  # re-open window
                    self.start_new(w)
                if self.btn_hint.handle_event(ev):  # reveal a letter
                    self.give_hint()
                if self.btn_scores.handle_event(ev):  # reveal scores panel
                    self.show_scores = True

    def give_hint(self):
        if self.won or self.lost:
            return
        # reveal one unrevealed letter (small penalty)
        unrevealed = [c for i, c in enumerate(self.secret) if self.display[i] == "_"]
        if not unrevealed:
            return
        letter = random.choice(unrevealed)
        self.propose_letter(letter)
        self.penalties = min(MAX_PENALTIES, self.penalties + 1)  # small penalty for hint
        self.info_message = f"Indice utilisé : '{letter}' (+1 pénalité)"

    def draw_scores_panel(self, surf):
        # panneau modal centré
        panel_w, panel_h = 400, 320
        panel_rect = pygame.Rect((WIDTH - panel_w) // 2, (HEIGHT - panel_h) // 2, panel_w, panel_h)
        pygame.draw.rect(surf, (240, 240, 240), panel_rect, border_radius=16)
        pygame.draw.rect(surf, (180, 180, 180), panel_rect, 3, border_radius=16)

        # bouton X
        self.btn_close_scores = Button(pygame.Rect(panel_rect.right - 40, panel_rect.top + 10, 30, 30),"X",FONT_SM,bg=(200, 80, 80),fg=(255, 255, 255),)
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
