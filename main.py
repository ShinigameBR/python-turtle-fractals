import turtle
import time
from lsystem import LSystem
from funcs import setup_window, setup_pencil
from fractals import draw_fractal_honeycomb, draw_fractal_sierpinski_triangle

# Configurações da tela e do lápis
screen = turtle.Screen()
setup_window(screen, 600, 600)

pencil = turtle.Turtle()
setup_pencil(pencil, 3, 1, 'orange')


# Criação do LSystem
#l_system_1 = LSystem("A", {"A": "AB","B": "A",}, 60)
l_system_2 = LSystem("F", {"F": "F-G+F+G-F","G": "GG",}, 120)

# Desenho do fractal
for gen in range(1, 21):  # Gerações de 1 a 20
    screen.clear()
    setup_window(screen, 600, 600)
    setup_pencil(pencil, 3, 1, 'orange')
    screen.title(f"Geração: {gen}")
    
    # Tipo de fractal
    #draw_fractal_honeycomb(pencil, l_system_1, gen)
    draw_fractal_sierpinski_triangle(pencil, l_system_2, gen)
    
    # Pausa para ver a geração
    time.sleep(3)

# Manter a janela aberta para última geração
turtle.done()