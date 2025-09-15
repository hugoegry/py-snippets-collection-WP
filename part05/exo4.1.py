invite: list[str] = ['mike', 'hugo']
p: str = input()
if p in invite:
    print(f'Bienvenue {p}')
else:
    print("perds-toi !")
