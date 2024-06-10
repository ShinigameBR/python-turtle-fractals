import turtle
from lsystem import LSystem

def draw_fractal_honeycomb(pencil: turtle.Turtle, l_system: LSystem, generation: int):
    instructions = l_system.generate(generation)
    for command in instructions:
        if command == 'A':
            pencil.left(l_system.angle)
            pencil.forward(20)
        elif command == 'B':
            pencil.right(l_system.angle)
            pencil.forward(20)
            
def draw_fractal_sierpinski_triangle(pencil: turtle.Turtle, l_system: LSystem, generation: int):
    instructions = l_system.generate(generation)
    for command in instructions:
        if command == 'F':
            pencil.forward(20)
        elif command == 'G':
            pencil.forward(20)  
        elif command == '+':
            pencil.left(l_system.angle)
        elif command == '-':
            pencil.right(l_system.angle)
            
def draw_fractal_hilbert(pencil: turtle.Turtle, l_system: LSystem, generation: int):
    instructions = l_system.generate(generation)
    for command in instructions:
        if command == 'F':
            pencil.forward(20)
        elif command == '+':
            pencil.right(l_system.angle)
        elif command == '-':
            pencil.left(l_system.angle)

def draw_fractal_koch(pencil: turtle.Turtle, l_system: LSystem, generation: int):
    instructions = l_system.generate(generation)
    for command in instructions:
        if command == 'F':
            pencil.forward(10)
        elif command == '+':
            pencil.right(l_system.angle)
        elif command == '-':
            pencil.left(l_system.angle)

def draw_fractal_pythagoras(pencil: turtle.Turtle, l_system: LSystem, generation: int):
    instructions = l_system.generate(generation)
    stack = []
    for command in instructions:
        if command == '1':
            pencil.forward(10)
        elif command == '0':
            pencil.forward(10)
        elif command == '[':
            stack.append((pencil.position(), pencil.heading()))
        elif command == ']':
            position, heading = stack.pop()
            pencil.penup()
            pencil.goto(position)
            pencil.setheading(heading)
            pencil.pendown()

def draw_fractal_barnsley(pencil: turtle.Turtle, l_system: LSystem, generation: int):
    instructions = l_system.generate(generation)
    stack = []
    pencil.goto(0, -500)
    pencil.setheading(90)
    for command in instructions:
        if command == 'X':
            pencil.setheading(0)
        if command == 'F':
            pencil.forward(10)
        elif command == '-':
            pencil.right(l_system.angle)
        elif command == '+':
            pencil.left(l_system.angle)
        elif command == '[':
            stack.append((pencil.position(), pencil.heading()))
        elif command == ']':
            position, heading = stack.pop()
            pencil.penup()
            pencil.setheading(heading)
            pencil.goto(position)
            pencil.pendown()
            
