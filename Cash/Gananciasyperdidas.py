registros = {}   


def registrar_ganancias():
    dia = input("Ingrese el día: ")

    if dia not in registros:
        registros[dia] = {"ganancias": [], "perdidas": []}

    monto = float(input("Monto de la ganancia: "))
    resumen = input("Ingrese un resumen o descripción: ")

    registros[dia]["ganancias"].append({"monto": monto, "resumen": resumen})
    print("Ganancia registrada.")


def registrar_perdidas():
    dia = input("Ingrese el día: ")

    if dia not in registros:
        registros[dia] = {"ganancias": [], "perdidas": []}

    monto = float(input("Monto de la pérdida: "))
    resumen = input("Ingrese un resumen o descripción: ")

    registros[dia]["perdidas"].append({"monto": monto, "resumen": resumen})
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

    total_g = sum(a["monto"] for a in datos["ganancias"])
    total_p = sum(a["monto"] for a in datos["perdidas"])

    print("\n--- RESUMEN DEL DÍA ---")
    print("Día:", dia)
    print("------------------------")

    # Mostrar ganancias detalladas
    if datos["ganancias"]:
        print("\nGANANCIAS:")
        for g in datos["ganancias"]:
            print(f"- ${g['monto']}: {g['resumen']}")
        print("Total ganancias:", total_g)

    # Mostrar pérdidas detalladas
    if datos["perdidas"]:
        print("\nPÉRDIDAS:")
        for p in datos["perdidas"]:
            print(f"- ${p['monto']}: {p['resumen']}")
        print("Total pérdidas:", total_p)

    print("\nBALANCE FINAL:", total_g - total_p)
    print("------------------------")