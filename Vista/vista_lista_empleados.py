import pyfiglet
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import Controlador.controlador_de_opciones as Control

def titulo():
    print("="*155)
    print(pyfiglet.figlet_format("Empleados en la empresa",width=155,justify="center"))
    print("="*155)


def lista_empleados():
    titulo()
    opcion=Control.procesar_vista_empleados()
    return opcion


if __name__ == "__main__":
    lista_empleados()