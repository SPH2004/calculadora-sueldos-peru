import os
import sys
import msvcrt
import pyfiglet

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Modelo.salida import salida_por_trabajador,salida_final
from Controlador import Utillidades
from Vista import vista_inicio,vista_lista_empleados,vista_principal



def procesar_opcion_menu_principal():
    cont=0
    while True:
        opcion=(msvcrt.getch().decode('utf-8'))
    
        if opcion=="0":     #Salir del programa
            cont=0
            return "Salida"
            break
        elif opcion=="1":   #Ver lista actual de empleados
            cont=0
            return "lista empleados"
            break
        elif opcion=="2":   #Agregar un nuevo empleado
            cont=0
            break
        elif opcion=="3":   #Informacion acerca de los descuentos
            cont=0
            break
        elif opcion=="4":   #Ver reporte del estado de pagos
            cont=0
            break
        else:
            if cont==0:
                print("Elija una opcion valida")
                cont=cont+1
            elif cont>=1:
                Utillidades.limpiar_linea(f"Elija una opcion valida...      x{cont}",0)
                cont=cont+1

def procesar_vista_empleados():
    cont=0
    while True:
        opcion=(msvcrt.getch().decode('utf-8'))
        if opcion=="0":     #Salir del programa
            cont=0
            return "principal"
            break
        elif opcion=="1":   #Ver lista actual de empleados
            cont=0
            return "lista empleados"
            break
        elif opcion=="2":   #Agregar un nuevo empleado
            cont=0
            break
        elif opcion=="3":   #Informacion acerca de los descuentos
            cont=0
            break
        elif opcion=="4":   #Ver reporte del estado de pagos
            cont=0
            break
        else:
            if cont==0:
                print("Elija una opcion valida")
                cont=cont+1
            elif cont>=1:
                Utillidades.limpiar_linea(f"Elija una opcion valida...      x{cont}",0)
                cont=cont+1
