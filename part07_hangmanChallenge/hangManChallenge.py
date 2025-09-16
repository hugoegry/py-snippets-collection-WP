"""
📌 Hangman Game in Python
A simple console-based Hangman game implemented in Python. Features random word selection, letter-by-letter guessing, and a dynamic game state display.
"""

import random
import os
from english_words import english_words_lower_alpha_set

secrets_worlds: str = ""
secrets_world_display: str = ""
nb_penaltie: int = 0
nb_essais: int = 0
proposed_letters: list = []
proposed_words: list = []
nb_penaltie_max: int = 6
nb_good_letters: int = 0


def get_random_word() -> str:
    return random.choice(list(english_words_lower_alpha_set))

def checkWord(word: str):
    global secrets_worlds
    return word == secrets_worlds

def checkLetterInWord(letter: str, word: str):
    global secrets_world_display
    if letter in word:
        for i , l in enumerate(word):
            if l == letter:
                secrets_world_display = secrets_world_display[:i] + letter + secrets_world_display[i+1:]
        return True
    return False

def print_hangman(nb_penaltie: int): # tete 1coup 1corp 2 bras 2 jambe
    print(f"vous avez {nb_penaltie} pénalité \n")
    print(" _______")
    print(" |     |")
    print(" |     " + ("O" if nb_penaltie >= 1 else ""))
    print(" |    " + ("/" if nb_penaltie >= 3 else " ") + ("|" if nb_penaltie >= 2 else " ") + ("\\" if nb_penaltie >= 4 else " "))
    print(" |     "+ ("|" if nb_penaltie >= 2 else " "))
    print(" |    " + ("/" if nb_penaltie >= 5 else " ") + (" \\" if nb_penaltie >= 6 else " "))
    print(" |")
    print("_|_")
    print()


def clear_console():
    print("\033c", end="")


def game_process():
    global secrets_worlds, secrets_world_display, nb_good_letters, nb_penaltie_max, proposed_words, proposed_letters, nb_essais, nb_penaltie
    if nb_penaltie >= nb_penaltie_max:
        print_hangman(nb_penaltie)
        print(f"Dommage ! Vous avez atteint le nombre maximum de pénalités. Le mot était {secrets_worlds}. \nFin de la partie")
        return
    if nb_good_letters == len(secrets_worlds):
        print(f"Félicitations ! Vous avez deviné le mot {secrets_worlds} en {nb_essais} essais avec {nb_penaltie} pénalités. \n Fin de la partie")
        return

    print(f"Mot à deviner : {secrets_world_display}")
    print_hangman(nb_penaltie)
    print(f"Lettres proposées : {', '.join(proposed_letters)}")
    input_user: str = input("Proposez une lettre ou un mot : ").lower()
    if input_user in proposed_letters or input_user in proposed_words:
        clear_console()
        print("Vous avez déjà proposé cette lettre ou ce mot. Essayez à nouveau.")
        game_process()
    if len(input_user) == 1:
        proposed_letters.append(input_user)
        if checkLetterInWord(input_user, secrets_worlds):
            nb_good_letters += 1
            nb_essais += 1
            clear_console()
            print(f"Bien joué ! La lettre {input_user} est dans le mot.")
        else:
            nb_essais += 1
            nb_penaltie += 1
            clear_console()
            print(f"Raté ! Vous avez {nb_penaltie} pénalités.")
    else:
        proposed_words.append(input_user)
        if checkWord(input_user):
            print("Félicitations ! Vous avez deviné le mot.")
            print(f"Vous avez trouvé le mot {secrets_worlds} en {nb_essais} essais avec {nb_penaltie} pénalités. \nFin de la partie")
            pass
        else:
            nb_essais += 1
            nb_penaltie += 5
            clear_console()
            print(f"Raté ! Vous avez {nb_penaltie} pénalités.")
    game_process()

def starGame():
    global secrets_world_display, secrets_worlds
    print("Bienvenue dans notre partie de jeux du pendu !")
    print("Configuration de la partie :")
    if input("Joueur 1 Voulez vous choisir un mot (o/n) ? ").lower() == "n":
        secrets_worlds = get_random_word().lower()
    else:
        secrets_worlds = input("Joueur 1 Choisissez un mot : ").lower()
    secrets_world_display = "_" * len(secrets_worlds)
    clear_console()
    game_process()


starGame()