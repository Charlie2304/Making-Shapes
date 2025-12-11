# [Making Shapes]
# [Charlie Smith]
# [11/12/25]
# AS Computer Science

# Imports

import turtle

# Global Variables

t = turtle.Turtle()
sides = 0
angles = 0
angle = 0

# Main Program

sides = int(input("How many sides do you want the shape to have?"))
angles = (sides - 2) * 180
angle = 360 / sides

print(sides, angles, angle)

for i in range(sides):
    t.forward(100)
    t.right(angle)
