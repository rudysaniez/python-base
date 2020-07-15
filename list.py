
##################
# Example 1 : Parcours d'une liste en utilisant la fonction len()
##################
days = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
print(days[0], len(days), len(days[0]))

i=0
while(i < len(days)):
    print(" > " + days[i])
    i = i + 1

###
# Example 2 : utilisation de la function eval
###
print("Ce script recherche le plus grand de trois nombres")
num = input("Veuillez saisir 3 nombres séparés par des virgules : ")
listOfValues = eval(num)
count = len(listOfValues)

i=0
while(i < count):
    print("Vous avez saisi", listOfValues[i])
    i = i + 1

###
# Example 3
###
value = input("Veuillez saisir une addition ou une soustraction :")
print("Voici le résultat :", eval(value))

empty=False
if not empty:
    print("gagné")
else:
    print("perdu")
