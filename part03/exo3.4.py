chUser: str = input("saisir une chaîne : ")
chUsers = chUser.split(" ")
ch: str = ""
for chUser in chUsers:
    chUser = chUser[0]
    ch += chUser
print(ch)
