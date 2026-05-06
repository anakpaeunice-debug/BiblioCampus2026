import json
import os

DATA_FILE = "data/library.json"

def charger_donnees():
    if not os.path.exists(DATA_FILE):
        return {"livres": [], "emprunts": []}
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def sauvegarder_donnees(donnees):
    os.makedirs("data", exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(donnees, f, indent=4, ensure_ascii=False)