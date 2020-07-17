#######################################
# IMPORTS
from turtle import *
from math import *
#######################################

#######################################
# NOTES
#
# reset()
# goto(x, y)
# forward(distance)
# backward(distance)
# up()
# down()
# color(string)
# left(angle)
# right(angle)
# width(épaisseur)
# fill(1) remplir un contour fermé à l'aide de la couleur sélectionnée
# write(string)
#######################################

#######################################
# CALCULS
print(" > pi = " + str(pi))
print(" > air d'un cercle (r=5cm) : pi * r * r -> ", pi * 5**2, "cm2")
print(" > périmétre d'un cercle (r=5cm) : 2 * pi * r", 2 * pi * 5, "cm")

# Aire d'un triangle A=(B * H)/2
aire = (7 * 4) / 2
print(" > L'aire d'un triangle", "=", "(B*H)/2", "(7 * 4) / 2", "=", aire, "cm2")

# Un rectangle, c'est tout d'abord deux triangles rectangles.
# L'aire d'un rectangle longeur * largeur, pour un triangle rectangle se sera (L * l) / 2
print(" > L'aire d'un triangle rectangle, c'est un rectangle d'une (Longeur de 10 et d'une Largeur de 5) / 2", "=", 
    (10 * 5) / 2, "cm2")
#######################################

#######################################
# LOCALES FUNCTIONS

# Write a letter.
# param letter : A, B, C or D
# param forwardOrBackward : 0=forward, 1=backward
def write_letter(letter, forward_or_backward):
    up()

    if forward_or_backward:
        backward(decalage)
    else:
        forward(decalage)

    write(letter)

    if forward_or_backward:
        forward(decalage)
    else:
        backward(decalage)

    down()


# Write a rectangle
# param longueur
# param hauteur
# param deltaWriteLetter
def display_rectangle(longueur, hauteur):

    write_letter("A", 1)
    forward(longueur)

    write_letter("B", 0)
    right(90)
    forward(hauteur)

    write_letter("C", 0)
    right(90)
    forward(longueur)

    write_letter("D", 0)
    right(90)
    forward(hauteur)


# Triangle rectangle en A, soit a2 + b2 = c2
# soit sqrt(a**2 + b**2) = c
# param a
# param b 
# link https://fr.wikihow.com/calculer-la-longueur-de-l%27hypoténuse
def hypotenuse(a, b):
    return sqrt(a**2 + b**2)


def aire_triangle(base, hauteur):
    return (base * hauteur) / 2

#######################################

#######################################
# APPLICATION
#
# Soit un triangle A(90°), B et C. Arc tangente b = ac / ab (triangle rectangle en a).
# atan (5/7)= 0.6202494859828215 radians -> degrees(atan(5,7)) = 35°
# https://www.assistancescolaire.com/eleve/3e/maths/reviser-une-notion/calculer-la-mesure-d-un-angle-dans-un-triangle-rectangle-3mtr07

# Trace un rectangle
longueur = 200
hauteur = 80
decalage=10

display_rectangle(longueur, hauteur)

right(90) #se repositionne à 90 afin de tracer une ligne horizontale

# Trace l'hypoténuse (a**2 = b**2 + c**2, par exemple 3**2 + 4**2 = 5**2)
# Le calcule de l'angle c, tan c=ab/ac soit longueur/hauteur.
# Mais le tracé de l'angle démarre de l'extérieur, donc c'est 90 - degrees(atan(ab/ac))
# Ce qui revient à calculer l'angle b, tan b=ac/ab soit hauteur/longueur
right(90 - degrees(atan(longueur/hauteur)))
color("red")
forward( hypotenuse(longueur, hauteur) ) #Hypoténuse= a2 = b2 + c2 -> sqrt(b2 + c2) = hypoténuse

# Triangle rectangle en A, l'angle b=ac/ab = tan b -> inv tan(b) en radian
# Triangle rectangle en A, l'angle c=ab/ac = tan c -> inv tan(c) en radian
print("Angle b = ", degrees(atan(hauteur/longueur)))
print("Angle c = ", degrees(atan(longueur/hauteur)))
print("L'hypothénuse =", sqrt(longueur**2 + hauteur**2))
print("Le périmetre =", longueur + hauteur + sqrt(longueur**2 + hauteur**2))

# Repositionnement, pour tracer un triangle rectangle
right(degrees(atan(longueur/hauteur))) # la direction est vers le bas, on va ajouter 90°.
right(90)
up() # on relève le crayon.
forward(longueur + longueur) # on s'éloigne de l'angle A (90°) de <longueur> en pixel

color("blue")
ac=hauteur
ab=120
hypotenuse=sqrt(ac**2 + ab**2)

down() # on repose le crayon
right(90)
forward(hauteur)
right(90) # on se positionne à l'horizontal
right(90 - degrees(atan(ab / ac)))
forward(hypotenuse)
right(degrees(atan(ab/ac)) + 90)
forward(ab)

# Ecriture des angles soit A, B et C
decalage=10
up()
forward(decalage)
color("black")
write("A")

right(90)
forward(ac);
write("C")

right(90)
forward(decalage)
right(90 - degrees(atan(ab/ac)))

forward(hypotenuse + decalage)

write("B")
backward(decalage)
left(degrees(atan(ac/ab)))
left(90)

mainloop()
