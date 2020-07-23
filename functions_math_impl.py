from functions_math import *

up()
goto(-250, 250)
down()

display_triangle_equilateral(60)
space()
display_triangle_rectangle(50, 20)
space()
display_rectangle(80, 40)
space()
display_rectangle(50, 50)
space()
display_star(60)

up();goto(-250, 150);down()

display_triangle_equilateral(60, 0, 0, "C")
space()
display_triangle_equilateral(50, 0, 1, "B")
space(25)
display_triangle_equilateral(50, 0, 1, "B")
space(25)
display_triangle_equilateral(50, 0, 0, "B")
space(25)
display_triangle_equilateral(50, 0, 1, "C")
up();left(90);forward(50);right(90);down();
display_triangle_equilateral(50, 0, 1, "C")
space(25)
display_triangle_equilateral(60, 0, 0, "C")

up();goto(-250, 0);down()

display_star(80)
space(25)
display_star(60)
space(25)
display_star(40)
space(25)
display_star(20)



mainloop()