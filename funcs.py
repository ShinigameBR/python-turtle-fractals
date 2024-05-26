import turtle

def setup_window(screen: turtle._Screen, width: int, height: int):
    screen.setup(width, height)
    screen.screensize(3 * width, 3 * height)
    screen.bgcolor('black')
    screen.delay(0)
    
def setup_pencil(pencil: turtle.Turtle, pensize: int, speed: int, color: str):
    pencil.pensize(pensize)
    pencil.speed(speed)
    pencil.color(color)
    pencil.penup()
    pencil.goto(0, 0)
    pencil.pendown()
