# highscores_inc.py
import json
import os
from datetime import datetime
from typing import List, Dict

DEFAULT_FILE = "highscores.json"


class HighScoreManager:
    """
    Gestion des meilleurs scores dans un fichier JSON.
    Stocke les 10 meilleurs scores, chacun avec:
    - name (str)
    - score (int)
    - attempts (int)
    - penalties (int)
    - date
    """

    def __init__(self, file_path: str = DEFAULT_FILE, top_n: int = 10):
        self.file_path = file_path
        self.top_n = top_n
        self.scores: List[Dict] = []
        self._load()

    def _load(self):
        if not os.path.exists(self.file_path):
            self.scores = []
            return
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                self.scores = json.load(f)
        except Exception:  # si fichier corrompu = reset
            self.scores = []

    def _save(self):
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(self.scores, f, ensure_ascii=False, indent=2)

    def get_top(self, n: int = None) -> List[Dict]:
        if n is None:
            n = self.top_n
        return self.scores[:n]

    def qualifies(self, score: int) -> bool:
        if len(self.scores) < self.top_n:
            return True
        return score > self.scores[-1]["score"]

    def insert(self, name: str, score: int, attempts: int, penalties: int):
        entry = {
            "name": name,
            "score": int(score),
            "attempts": int(attempts),
            "penalties": int(penalties),
            "date": datetime.utcnow().isoformat(timespec="seconds") + "Z",
        }
        self.scores.append(entry)
        self.scores.sort(key=lambda x: (-x["score"], x["date"]))  # tri descendant par score puis par date
        self.scores = self.scores[: self.top_n]  # garde top N
        self._save()
