
username = input("Veuillez saisir votre prénom : ")
if(len(username) == 0):
    print("Le prénom est obligatoire pour continuer...", "\n", "Au revoir.")
else:
    print("Bonjour", username)

    result = input("Combien font 46 + 4 = ")
    if(int(result) == 50):
        print("C'est bien " + username)
    else: print("Domage, le résultat est ", str(46+4))