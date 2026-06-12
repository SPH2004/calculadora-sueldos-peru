# Importacion
from calculos import calcular_descuento
from regimen import filtrar_regimen
from salida import salida_por_trabajador,salida_final

def main():
    total_trabajadores = 0
    total_sueldos_netos = 0.0
    status = True

    while status:
        sueldo_base = float(input("Ingrese el sueldo bruto: "))
        print("\nRégimen pensionario:\n  1. AFP (10%)\n  2. ONP (13%)")

        regimen = filtrar_regimen(input("Elija una opción: "))
        descuento = calcular_descuento(sueldo_base, regimen)
        sueldo_neto = sueldo_base - descuento

        salida_por_trabajador(regimen, sueldo_base, descuento, sueldo_neto)

        total_trabajadores += 1
        total_sueldos_netos += sueldo_neto

        respuesta = input("\n¿Calcular otro trabajador? (s/n): ")
        status = respuesta == "s"
        if respuesta not in ["s", "n"]:
            print("Valor incorrecto, finalizando sesión.")

    salida_final(total_trabajadores, total_sueldos_netos)

main() 