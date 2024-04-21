# import color gram
#
# colors = color gram.extract("image.jpg",25)
#
# color_list = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_tuple = (r, g, b)
#     color_list.append(color_tuple)
#
# print(color_list)

import random
import turtle as t

t.colormode(255)
tim = t.Turtle()
tim.shape("arrow")

color_list = [(224, 171, 128), (146, 180, 192), (45, 104, 160), (124, 82, 93), (184, 147, 158), (129, 73, 54),
              (218, 230, 221), (38, 49, 66), (114, 174, 125), (177, 102, 150), (71, 6, 22), (43, 132, 104),
              (212, 79, 58), (236, 186, 137), (79, 96, 187), (66, 53, 43), (213, 177, 186), (113, 43, 55),
              (176, 184, 215), (226, 177, 164), (71, 64, 53), (174, 203, 183)]
tim.penup()
tim.hideturtle()
tim.speed("fastest")
tim.setheading(225)  # (270-180) / 2 = (45+180) = 225
tim.forward(300)
tim.setheading(0)
print(tim.position())
for n in range(1, 11):
    for _ in range(1, 11):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)
    # tim.home()
    # tim.left(90)
    # tim.forward(n*50)
    # tim.right(90)
    tim.goto(-212.13, (-212.13 + (n * 50)))

screen = t.Screen()
screen.exitonclick()


# Angela's code
# import turtle as turtle_module
# import random
#
# turtle_module.colormode(255)
# tim = turtle_module.Turtle()
# tim.speed("fastest")
# tim.penup()
# tim.hideturtle()

# color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40),
# (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233,
# 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148,
# 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]

# tim.setheading(225)
# tim.forward(300)
# tim.setheading(0)
# number_of_dots = 100
#
# for dot_count in range(1, number_of_dots + 1):
#     tim.dot(20, random.choice(color_list))
#     tim.forward(50)
#
#     if dot_count % 10 == 0:
#         tim.setheading(90)
#         tim.forward(50)
#         tim.setheading(180)
#         tim.forward(500)
#         tim.setheading(0)
