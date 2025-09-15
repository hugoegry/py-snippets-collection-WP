arborescence = {
    "mon_projet": {
        "README.md": None,
        "main.py": None,
        "requirements.txt": None,
        "docs": {"introduction.md": None, "architecture.md": None},
        "src": {
            "utils.py": None,
            "data": {"dataset.csv": None, "preprocess.py": None},
            "models": {"model.py": None, "trainer.py": None},
        },
        "tests": {
            "test_main.py": None,
            "test_utils.py": None,
            "test_models": {"test_trainer.py": None},
        },
    }
}

def list_directorie(directorie: dict, prefix = ""):
    for k, v in directorie.items():
        print(f"{prefix}{k}")
        if v != None:
            list_directorie(v, prefix + "  ")


list_directorie(arborescence)
