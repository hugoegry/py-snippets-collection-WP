from math import sqrt

alphabetMondial: dict = {
    'a': {'france': 7.6, 'espagne': 12.5, 'allemand': 6.5, 'anglais': 8.2},
    'b': {'france': 0.9, 'espagne': 1.5, 'allemand': 1.9, 'anglais': 1.5},
    'c': {'france': 3.3, 'espagne': 4.0, 'allemand': 3.0, 'anglais': 2.8},
    'd': {'france': 3.6, 'espagne': 5.0, 'allemand': 5.1, 'anglais': 4.3},
    'e': {'france': 14.7,'espagne': 13.7, 'allemand': 17.4, 'anglais': 12.7},
    'f': {'france': 1.1, 'espagne': 0.7, 'allemand': 1.7, 'anglais': 2.2},
    'g': {'france': 1.0, 'espagne': 1.0, 'allemand': 3.0, 'anglais': 2.0},
    'h': {'france': 0.7, 'espagne': 0.7, 'allemand': 4.8, 'anglais': 6.1},
    'i': {'france': 7.5, 'espagne': 6.2, 'allemand': 7.6, 'anglais': 7.0},
    'j': {'france': 0.6, 'espagne': 0.5, 'allemand': 0.3, 'anglais': 0.2},
    'l': {'france': 5.5, 'espagne': 5.2, 'allemand': 3.4, 'anglais': 4.0},
    'm': {'france': 2.7, 'espagne': 3.2, 'allemand': 2.5, 'anglais': 2.4},
    'n': {'france': 7.2, 'espagne': 7.0, 'allemand': 9.8, 'anglais': 6.7},
    'o': {'france': 5.8, 'espagne': 8.7, 'allemand': 2.5, 'anglais': 7.5},
    'p': {'france': 3.0, 'espagne': 2.5, 'allemand': 0.8, 'anglais': 1.9},
    'q': {'france': 1.4, 'espagne': 1.0, 'allemand': 0.0, 'anglais': 0.1},
    'r': {'france': 6.5, 'espagne': 6.9, 'allemand': 7.0, 'anglais': 6.0},
    's': {'france': 7.9, 'espagne': 7.9, 'allemand': 7.3, 'anglais': 6.3},
    't': {'france': 7.0, 'espagne': 4.6, 'allemand': 6.2, 'anglais': 9.1},
    'u': {'france': 6.3, 'espagne': 3.9, 'allemand': 4.3, 'anglais': 2.8},
    'v': {'france': 1.8, 'espagne': 1.0, 'allemand': 0.8, 'anglais': 1.0},
    'w': {'france': 0.0, 'espagne': 0.0, 'allemand': 1.9, 'anglais': 2.4},
    'x': {'france': 0.4, 'espagne': 0.1, 'allemand': 0.0, 'anglais': 0.2},
    'y': {'france': 0.3, 'espagne': 1.0, 'allemand': 0.0, 'anglais': 2.0},
    'z': {'france': 0.1, 'espagne': 0.5, 'allemand': 1.1, 'anglais': 0.1},
    'ß': {'france': 0.0, 'espagne': 0.0, 'allemand': 0.3, 'anglais': 0.0},
    'ñ': {'france': 0.0, 'espagne': 0.3, 'allemand': 0.0, 'anglais': 0.0},
}

def textCleaner(text: str) -> str:
    text: str = text.lower()
    cText: str = ''
    for l in text:
        if l in alphabetMondial:  # si la lettre est dans le dictionnaire, on l'ajoute
            cText += l
    return cText


def lettreFrequences(texte: str) -> dict:
    counts: dict = {}
    total: int = 0
    
    for c in texte: # compter le nb fois ou une lettre apparait
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1

    for v in counts.values(): # garde que les val [1,2,3...]
        total += v
    
    freqs: dict = {}
    if total > 0: # Calculer les freq en %
        for c in counts:
            freqs[c] = counts[c] / total * 100
    return freqs

def distance(freqs, langue):
    s: float = 0.0
    for c in alphabetMondial:
        f_text: float = freqs.get(c, 0) # si c existe on le prend sinon 0
        f_lang: float = alphabetMondial[c].get(langue, 0)
        diff: float = f_text - f_lang
        s += diff * diff # passe au ² pour eviter les valeur n
    return sqrt(s) # racine carre de la somme


def detectLangue(text: str):
    cText: str = textCleaner(text)
    freqs: dict = lettreFrequences(cText)
    langues = set() # col

    for d in alphabetMondial.values(): # parcourir toutes les lettres dans alphabetMondial
        for langue in d: # parcourir toutes les langues pour cette lettre
            langues.add(langue)
    
    distances = {}
    for langue in langues:
        distances[langue] = distance(freqs, langue) 
    return min(distances, key=distances.get) # plus petite val de dist

print('Langue détectée : ', detectLangue(input()))




# text fr// Je m’appelle Jessica. Je suis une fille, je suis française et j’ai treize ans. Je vais à l’école à Nice, mais j’habite à Cagnes-Sur-Mer. J’ai deux frères.
# text esp//  es deliciosa y son famosos el gazpacho, el rebujito y el salmorejo.Yo vivo en Granada, una ciudad pequeña que tiene monumentos muy importantes como la Alhambra. Aquí la comida
# text all// Mein Name ist Anna. Ich komme aus Österreich und lebe seit drei Jahren in Deutschland. Ich bin 15 Jahre alt und habe zwei Geschwister: Meine Schwester heißt Klara und ist 13 Jahre alt, mein Bruder Michael