registros = {}   


def registrar_ganancias():
    dia = input("Ingrese el día: ")

    if dia not in registros:
        registros[dia] = {"ganancias": [], "perdidas": []}

    monto = float(input("Monto de la ganancia: "))
    registros[dia]["ganancias"].append(monto)
    print("Ganancia registrada.")


def registrar_perdidas():
    dia = input("Ingrese el día: ")

    if dia not in registros:
        registros[dia] = {"ganancias": [], "perdidas": []}

    monto = float(input("Monto de la pérdida: "))
    registros[dia]["perdidas"].append(monto)
    print("Pérdida registrada.")


def seleccionar_dia():
    if not registros:
        print("No hay días registrados.")
        return None

    dias = list(registros)
    print("\nDÍAS REGISTRADOS:")
    for i, d in enumerate(dias, 1):
        print(f"{i}. {d}")

    op = int(input("Seleccione el número del día: "))
    if 1 <= op <= len(dias):
        return dias[op - 1]
    return None


def mostrar_resumen():
    dia = seleccionar_dia()
    if dia is None:
        print("Opción inválida.")
        return

    datos = registros[dia]
    total_g = sum(datos["ganancias"])
    total_p = sum(datos["perdidas"])

    print("\n--- RESUMEN ---")
    print("Día:", dia)
    if total_g > 0:
        print("Total ganancias:", total_g)
    if total_p > 0:
        print("Total pérdidas:", total_p)
    print("Balance final:", total_g - total_p)
    print("--------------")

 #menu
def mostrar_menu():
    print("\nMENU PRINCIPAL")
    print("1. Registrar ganancias")
    print("2. Registrar pérdidas")
    print("3. Mostrar resumen de un día")
    print("4. Salir")

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_ganancias()
    elif opcion == "2":
        registrar_perdidas()
    elif opcion == "3":
        mostrar_resumen()
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida.")
        