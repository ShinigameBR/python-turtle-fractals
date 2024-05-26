import turtle
import time
from lsystem import LSystem
from funcs import setup_window, setup_pencil
from fractals import draw_fractal_honeycomb

# Configurações da tela e do lápis
screen = turtle.Screen()
setup_window(screen, 600, 600)

pencil = turtle.Turtle()
setup_pencil(pencil, 3, 1, 'orange')


# Criação do LSystem e geração do resultado
l_system = LSystem("A", {"A": "AB","B": "A",}, 60)

# Desenho do fractal
for gen in range(1, 21):  # Gerações de 1 a 20
    screen.clear()
    setup_window(screen, 600, 600)
    setup_pencil(pencil, 3, 1, 'orange')
    screen.title(f"Geração: {gen}")
    
    # Tipo de Fractal
    draw_fractal_honeycomb(pencil, l_system, gen)
    
    # Pausa para ver a geração
    time.sleep(3)

# Manter a janela aberta para última geração
turtle.done()