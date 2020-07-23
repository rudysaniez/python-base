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

print(" > pi = " + str(pi))
print(" > air d'un cercle (r=5cm) : pi * r * r -> ", pi * 5**2, "cm2")
print(" > périmétre d'un cercle (r=5cm) : 2 * pi * r", 2 * pi * 5, "cm")

print(" > L'aire d'un triangle", "=", "(B*H)/2", "(7 * 4) / 2", "=", (7 * 4) / 2, "cm2")

print(" > L'aire d'un triangle rectangle, c'est un rectangle d'une (Longeur de 10 et d'une Largeur de 5) / 2", "=", 
    (10 * 5) / 2, "cm2")


def write_letter(letter, forward_or_backward, delta):

    """
        Cette fonction écrit une lettre, par exemple A, B, C ou D, au positionnement courant.
        forward_or_backwaard : 0=forward, 1=backward.
    """

    up()

    if forward_or_backward:
        backward(delta)
    else:
        forward(delta)

    write(letter)

    if forward_or_backward:
        forward(delta)
    else:
        backward(delta)

    down()


def display_rectangle(longueur, hauteur, display_letter=0, angle_return="D"):

    "Cette fonction trace un rectangle à l'aide d'une longueur et d'une hauteur"

    if display_letter:
        write_letter("A", 1, 7)

    left(90)
    forward(hauteur)

    if display_letter:
        write_letter("B", 0, 5)

    right(90)
    forward(longueur)

    left(90)

    if display_letter:
        write_letter("C", 0, 5)

    right(180)
    forward(hauteur)

    if display_letter:
        left(90)
        write_letter("D", 0, 6)
        right(180)
    else :
        right(90)

    forward(longueur)

    if not angle_return or angle_return.upper().__eq__("D"):
        backward(longueur)
        right(180)
    elif angle_return.upper().__eq__("B"):
        right(90)
        forward(hauteur)
        right(90)
    elif angle_return.upper().__eq__("C"):
        right(90)
        forward(hauteur)
        right(90)
        forward(longueur)
    elif angle_return.upper().__eq__("A"):
        right(90 + 90)


def hypotenuse(a, b):

    "Calcul de l'hypoténuse, voir https://fr.wikihow.com/calculer-la-longueur-de-l%27hypoténuse"

    return sqrt(a**2 + b**2)


def aire_triangle(base, hauteur):

    "Calcul de l'aire d'un triangle"

    return (base * hauteur) / 2


def volume_sphere(rayon):

    "Calcul du volume d'une sphère"

    return (4 * pi * rayon**3) / 3


def display_triangle_rectangle(ab, ac, display_letter=0, angle_return="C"):

    """ Triangle rectangle en A. Les angles b et c se calculent avec la function angle_triangle_rectangle """

    if display_letter:
        write_letter("A", 1, 8)

    left(90)
    forward(ac)

    if display_letter:
        write_letter("C", 0, 5)

    right(90)
    right(90 - angle_triangle_rectangle(ab, ac, "C"))
    forward(hypotenuse(ac, ab))

    left(angle_triangle_rectangle(ab, ac, "B"))

    if display_letter:
        write_letter("B", 0, 5)

    right(180)
    forward(ab)

    up()

    if not angle_return or angle_return.upper().__eq__("C"):
        angle_return = "C"
        backward(ab)
        right(180)
    elif angle_return.upper().__eq__("B"):
        right(90)
        forward(ac)
        right(90)
    elif angle_return.upper().__eq__("A"):
        right(90 + 90)

    down()


def angle_triangle_rectangle(a_to_b, a_to_c, angle_named="B"):

    """Soit un triangle rectangle en A. L'angle B se calcule atan(ac/ab). L'angle C se calcule atan(ab/ac)."""

    if angle_named.upper().__eq__("B"):
        return degrees(atan(a_to_c / a_to_b))
    else:
        return degrees(atan(a_to_b / a_to_c))


def display_triangle_equilateral(longueur, display_letter=0, top_or_bot=0, angle_return="C"):

    """ Trace un triangle équilatéral, et repositionne le curseur sur l'angle A, B ou C """

    if display_letter:
        write_letter("A", 1, 10)

    if not top_or_bot:
        left(60)
    else:
        right(60)

    forward(longueur)

    if display_letter:
        left(30)
        write_letter("B", 0, 7)
        right(90)
    else:
        if not top_or_bot:
            right(60)
        else:
            left(60)

    if not top_or_bot:
        right(60)
    else:
        left(60)

    forward(longueur)

    if display_letter:
        left(60)
        write_letter("C", 0, 9)
        right(180)
    else :
        if not top_or_bot:
            right(120)
        else:
            left(120)

    forward(longueur)

    up()

    if not angle_return or angle_return.upper().__eq__("C"):
        angle_return = "C"
        backward(longueur)
        right(180)
    elif angle_return.upper().__eq__("B"):
        if not top_or_bot:
            right(90 + 30)
            forward(longueur)
            right(60)
        else:
            left(90 + 30)
            forward(longueur)
            left(60)
    elif angle_return.upper().__eq__("A"):
        right(90 + 90)

    down()


def display_star(longueur):

    display_triangle_equilateral(longueur, 0, 0, "A")
    left(90)
    up()
    forward(2 * (longueur/3))
    down()
    right(90)
    display_triangle_equilateral(longueur, 0, 1, "C")


def space(s=30):

    up()
    forward(s)
    down()


#######################################
# APPLICATION
#
# Soit un triangle A(90°), B et C. Arc tangente b = ac / ab (triangle rectangle en a).
# atan (5/7)= 0.6202494859828215 radians -> degrees(atan(5,7)) = 35°
# https://www.assistancescolaire.com/eleve/3e/maths/reviser-une-notion/calculer-la-mesure-d-un-angle-dans-un-triangle-rectangle-3mtr07


def demo():
    # Trace un rectangle
    longueur = 200
    hauteur = 80

    display_rectangle(longueur, hauteur)

    right(90)

    # Trace l'hypoténuse (a**2 = b**2 + c**2, par exemple 3**2 + 4**2 = 5**2)
    # Le calcule de l'angle c, tan c=ab/ac soit longueur/hauteur.
    # Mais le tracé de l'angle démarre de l'extérieur, donc c'est 90 - degrees(atan(ab/ac))
    # Ce qui revient à calculer l'angle b, tan b=ac/ab soit hauteur/longueur
    right(90 - degrees(atan(longueur/hauteur)))
    color("red")
    forward(hypotenuse(longueur, hauteur))

    # Triangle rectangle en A, l'angle b=ac/ab = tan b -> inv tan(b) en radian
    # Triangle rectangle en A, l'angle c=ab/ac = tan c -> inv tan(c) en radian
    print("Angle b =", degrees(atan(hauteur/longueur)))
    print("Angle c =", degrees(atan(longueur/hauteur)))
    print("Angle b =", angle_triangle_rectangle(longueur, hauteur, "B"))
    print("L'hypothénuse =", hypotenuse(longueur, hauteur))
    print("Le périmetre =", longueur + hauteur + sqrt(longueur**2 + hauteur**2))

    # Repositionnement, pour tracer un triangle rectangle
    right(degrees(atan(longueur/hauteur))) # la direction est vers le bas, on va ajouter 90°.
    right(90)

    up() # on relève le crayon.
    forward(longueur + longueur) # on s'éloigne de l'angle A (90°) de <longueur> en pixel

    ac=hauteur
    ab=120

    down()

    display_triangle_rectangle(ab, ac)


