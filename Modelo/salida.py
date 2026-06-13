import pyfiglet
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Controlador.Utillidades import limpiar_consola


def salida_por_trabajador(regimen, sueldo_base, descuento, sueldo_neto):
    print("-" * 33)
    print(f"Régimen:       {regimen[1]}")
    print(f"Sueldo bruto:  S/. {sueldo_base:.2f}")
    print(f"Descuento:     S/. {descuento:.2f}")
    print(f"Sueldo neto:   S/. {sueldo_neto:.2f}")

def salida_final(total_trabajadores, total_sueldos_netos):
    print("=" * 33)
    print("RESUMEN FINAL")
    print("=" * 33)
    print(f"Trabajadores procesados:  {total_trabajadores}")
    print(f"Total sueldos netos:      S/. {total_sueldos_netos:.2f}")
    print("=" * 33)

def lista_regimen():
    print("""
            Régimen pensionario:
            1. AFP (10%)
            2. ONP (13%)
          """)