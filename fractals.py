import turtle
from lsystem import LSystem

def draw_fractal_honeycomb(pencil: turtle.Turtle, l_system: LSystem, generations: int):
    instructions = l_system.generate(generations)
    for command in instructions:
        if command == 'A':
            pencil.left(l_system.angle)
            pencil.forward(20)
        elif command == 'B':
            pencil.right(l_system.angle)
            pencil.forward(20)
            
def draw_fractal_sierpinski_triangle(pencil: turtle.Turtle, l_system: LSystem, generations: int):
    instructions = l_system.generate(generations)
    for command in instructions:
        if command == 'F':
            pencil.forward(20)
        elif command == 'G':
            pencil.forward(20)  
        elif command == '+':
            pencil.left(l_system.angle)
        elif command == '-':
            pencil.right(l_system.angle)