maList = [
    ["Monday", "3:30 PM", "Joe", "Sam"],
    [ "Monday","4:30 PM", "Bob" , " Alice" ] ,
    [ "Tuesday" , "3:30 PM" , "Joe" , "Bob" , "Ali ce" , "Sam" ],
    [ "Tuesday" , "9:30 AM" , "Joe" , "Bob" ]
]
nom: str = input("nom : ").title()
prenom: str = input("prenom : ").title()
selectedReunion = []
for e in maList:
    if nom in e and prenom in e:
        selectedReunion.append(e)
        print(f"Vous avez une réunion le {e[0]} à {e[1]}")
# print(selectedReunion)

# 1 ligne (for)
# print([i for i in maList if nom in i and prenom in i])
