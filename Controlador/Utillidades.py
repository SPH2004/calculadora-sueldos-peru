import os
import time 
import pyfiglet
import msvcrt

def limpiar_consola():
    # 'nt' corresponde a Windows
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def cambiar_vista(vista):
    limpiar_consola()
    estado=vista
    return estado

def limpiar_linea(text,delay):
    LINE_UP = '\033[1A'
    LINE_CLEAR = '\x1b[2K'
    time.sleep(delay)
    print(f"{LINE_UP}{LINE_CLEAR}{text}")

def salir():
    for tiempo in range (3,0,-1):
        limpiar_consola()
        print(pyfiglet.figlet_format(f"Saliendo del programa en {tiempo}",font="small",width=155,justify="center"))
        time.sleep(1)
        if tiempo==1:
            limpiar_consola()
            exit()  # Cierra el programa de forma controlada


def comprobar_inicio():
    tecla=(msvcrt.getch().decode('utf-8'))
    if tecla=="\r":         #tecla enter
        limpiar_consola()
        return "principal"
    elif tecla == "\x1b":  # tecla Escape
        return "salida"