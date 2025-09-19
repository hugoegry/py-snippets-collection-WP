import os, json, random, csv, xml.etree.ElementTree as ET

# Tente d'importer un ensemble de mots anglais
# Si le module n'est pas dispo, on utilisera un fichier de secours
try:
    from english_words import english_words_lower_alpha_set as WORD_SET
except Exception:
    WORD_SET = None


def load_fallback_words(file_path="fallback_words.json"):
    """
    Charge un dictionnaire de mots de secours depuis un fichier.
    Supporte JSON, XML, TXT et CSV.
    """
    if not os.path.exists(file_path):
        return [
            "python",
            "ordinateur",
            "reseau",
            "securite",
            "developpeur",
            "hangman",
            "programmation",
            "interface",
            "design",
            "systeme",
            "pygame",
            "algorithme",
        ]

    ext = os.path.splitext(file_path)[1].lower()

    try:
        if ext == ".json":
            with open(file_path, "r", encoding="utf-8") as f:
                return json.load(f)

        elif ext == ".xml":
            print(f"Loading XML words from {file_path}")
            tree = ET.parse(file_path)
            root = tree.getroot()
            return [elem.text for elem in root.findall(".//word")]

        elif ext == ".txt":
            print(f"Loading TXT words from {file_path}")
            with open(file_path, "r", encoding="utf-8") as f:
                return [line.strip() for line in f if line.strip()]

        elif ext == ".csv":
            print(f"Loading CSV words from {file_path}")
            words = []
            with open(file_path, newline="", encoding="utf-8") as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    words.extend(row)  # prend toutes les colonnes
            return words

        else:
            raise ValueError(f"Extension de fichier non supportée: {ext}")

    except Exception as e:
        print(f"[ERREUR] Impossible de charger {file_path}: {e}")
        return ["python", "fallback", "erreur"]


def get_random_word(fallback_file="fallback_words.json"):
    if WORD_SET:
        return random.choice(list(WORD_SET))

    fallback_words = load_fallback_words(fallback_file)
    return random.choice(fallback_words)


def sanitize_word(w: str) -> str:
    return "".join(ch for ch in w.lower() if ch.isalpha())
