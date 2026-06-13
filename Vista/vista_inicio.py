import pyfiglet
import os
import sys
import msvcrt
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Controlador.Utillidades import limpiar_consola,comprobar_inicio
from Vista.vista_principal import menu_principal

def titulo():
    print("="   *   155)
    print(pyfiglet.figlet_format("Estudio Contable",font="roman",width=155,justify="center"))
    print(pyfiglet.figlet_format("Rios & Asociados",font="roman",width=155,justify="center"))
    print("="   *   155)
    print("Presiona ENTER para iniciar...")

def menu_inicio():
    while True:
        limpiar_consola()
        titulo()
        status= comprobar_inicio()
        return status

if __name__ == "__main__":
    menu_inicio()