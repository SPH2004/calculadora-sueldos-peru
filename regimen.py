def filtrar_regimen(tipo):
    afp = [1, "AFP", 0.10]
    onp = [2, "ONP", 0.13]

    if tipo == "1":
        return afp
    elif tipo == "2":
        return onp
    else:
        print("Opción inválida. Intente de nuevo.")
        exit()