
#---
# Calcul with Python
#---

print(4 + 3)
print( (2 - 9) + ( 9 -2))
print("Division réelle : " + str(20 / 3)) # Division réelle
print("Division entière : " + str(20 // 3)) # Division entière
print("Division avec un float : " + str(20.3 / 5))

# Variables

i = 7; j= 8 ; k = 2;
print("Résultat i + j - k = " + str(i + j - k))

x = y = 3;

print("(7 * 5.3) + (j + 2) = " + str((7 * 5.3) + (j + 2)))
print("7 * 3 + 5 + 2 = " + str(7 * 3 + 5 + 2))

print("Modulo 10%3 = " + str(10 % 3)) # Modulo (1)
print("Modulo 10%5 = " + str(10 % 5)) # Modulo (0)

# Note : Priorité des opérateurs -> PEMDAS (parenthèse, exposant, multiplication & division, addition & soustraction)

#---
# Exposant
#---
a=10
print("10 puissance 1 = " + str(a**1) + ", ", "10 puissance 2 = " + str(a**2))


# Séquence d'instructions
a, b = 3, 7;
a = b;
b = a;
print("a=" + str(a), "b=" + str(b))
