import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import Controlador.controlador_de_opciones as Control

def vista_principal():
    print("="*25,end="")
    print(" Bienvenido al panel del empleador ",end="")
    print("="*25)
    print("""
            Que desea realizar:
            (1): Ver lista actual de empleados
            (2): Agregar un nuevo empleado
            (3): Informacion acerca de los descuentos
            (4): Ver reporte del estado de pagos
            (0): Salir del programa
          """)
    print("="*85)

def menu_principal():
    vista_principal()
    opcion=Control.procesar_opcion_menu_principal()
    return opcion


    

if __name__ == "__main__":  
    menu_principal()
