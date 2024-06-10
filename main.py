import turtle
import time
import argparse
from lsystem import LSystem
from funcs import setup_window, setup_pencil
from fractals import *

# Configurações da tela
screen_size = 1000

# Configuração do argparse para obter o tipo de fractal e o número de gerações
parser = argparse.ArgumentParser(description="Escolha o tipo de fractal para desenhar.")
parser.add_argument(
    "fractal_type",
    choices=["honeycomb", "sierpinski", "hilbert", "koch", "pythagoras", "barnsley"],
    help="Tipo de fractal para desenhar: 'honeycomb', 'sierpinski', 'hilbert', 'koch', 'pythagoras', 'barnsley'"
)
parser.add_argument(
    "-g",
    type=int,
    default=20,
    help="Número de gerações para desenhar (padrão: 20)"
)
args = parser.parse_args()

# Inicialização da tela e do lápis
screen = turtle.Screen()
setup_window(screen, screen_size, screen_size)

pencil = turtle.Turtle()
setup_pencil(pencil, 3, 1, 'orange')

# Criação do LSystem
l_systems = {
    "honeycomb": LSystem("A", {"A": "AB","B": "A",}, 60),
    "sierpinski": LSystem("F", {"F": "F-G+F+G-F","G": "GG",}, 120),
    "hilbert": LSystem("A", {"A": "-BF+AFA+FB-", "B": "+AF-BFB-FA+"}, 90),
    "koch": LSystem("F", {"F": "F+F--F+F"}, 60),
    "pythagoras": LSystem("0", {"1": "11", "0": "1[0]0"}, 45),
    "barnsley": LSystem("X", {"X": "F+[[X]-X]-F[-FX]+X", "F": "FF"}, 25), # Ainda em progresso
}

draw_functions = {
    "honeycomb": draw_fractal_honeycomb,
    "sierpinski": draw_fractal_sierpinski_triangle,
    "hilbert": draw_fractal_hilbert,
    "koch": draw_fractal_koch,
    "pythagoras": draw_fractal_pythagoras,
    "barnsley": draw_fractal_barnsley,
}

# Desenho do fractal baseado no argumento fornecido
for gen in range(1, args.g + 1):  # Gerações de 1 a 20
    screen.clear()
    setup_window(screen, screen_size, screen_size)
    setup_pencil(pencil, 3, 1, 'orange')
    screen.title(f"{args.fractal_type.capitalize()} Fractal - Geração: {gen}")
    
    # Tipo de fractal
    draw_functions[args.fractal_type](pencil, l_systems[args.fractal_type], gen)
    
    # Pausa para ver a geração
    time.sleep(1)

# Manter a janela aberta para última geração
turtle.done()