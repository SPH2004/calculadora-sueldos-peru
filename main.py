# Importacion
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import Vista.vista_inicio as  vista_inicio
import Vista.vista_principal as  vista_principal
import Vista.vista_lista_empleados as vista_empleados
from Controlador.Utillidades import cambiar_vista, salir

def main():
    vista_actual="inicio"

    while True:
        if vista_actual=="inicio":
            vista_actual=cambiar_vista(vista_inicio.menu_inicio())
        elif vista_actual=="principal":
            vista_actual=cambiar_vista(vista_principal.menu_principal())
        elif vista_actual=="lista empleados":
            vista_actual=cambiar_vista(vista_empleados.lista_empleados())
        elif vista_actual=="salida":
            salir()








if __name__ == "__main__":
    main() 