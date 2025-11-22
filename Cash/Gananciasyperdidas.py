from datetime import datetime

registros = {}   


def registrar_ganancias():
    # Fecha actual en dia-mes-año
    dia = datetime.now().strftime("%d-%m-%Y")

    #si no existe se crea
    if dia not in registros:
        registros[dia] = {"ganancias": [], "perdidas": []}

    monto = float(input("Monto de la ganancia: "))
    resumen = input("Ingrese un resumen o descripción: ")

    # hora exacta en que se hizo  el reporte
    hora = datetime.now().strftime("%H:%M:%S")

    registros[dia]["ganancias"].append({
        "monto": monto,
        "resumen": resumen,
        "hora": hora
    })

    print(f"Ganancia registrada en la fecha {dia} a las {hora}.")


def registrar_perdidas():
    dia = datetime.now().strftime("%d-%m-%Y")

    if dia not in registros:
        registros[dia] = {"ganancias": [], "perdidas": []}

    monto = float(input("Monto de la pérdida: "))
    resumen = input("Ingrese un resumen o descripción: ")

    hora = datetime.now().strftime("%H:%M:%S")

    registros[dia]["perdidas"].append({
        "monto": monto,
        "resumen": resumen,
        "hora": hora
    })

    print(f"Pérdida registrada en la fecha {dia} a las {hora}.")


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
    # Suma de ganancias y pérdidas
    total_g = sum(a["monto"] for a in datos["ganancias"])
    total_p = sum(a["monto"] for a in datos["perdidas"])

    print("\n--- RESUMEN DEL DÍA ---")
    print("Día:", dia)
    print("------------------------")

    # Mostrar ganancias detalladas
    if datos["ganancias"]:
        print("\nGANANCIAS:")
        for g in datos["ganancias"]:
            print(f"- ${g['monto']}: {g['resumen']} (Hora: {g['hora']})")
        print("Total ganancias:", total_g)

    # Mostrar pérdidas detalladas
    if datos["perdidas"]:
        print("\nPÉRDIDAS:")
        for p in datos["perdidas"]:
            print(f"- ${p['monto']}: {p['resumen']} (Hora: {p['hora']})")
        print("Total pérdidas:", total_p)

    print("\nBALANCE FINAL:", total_g - total_p)
    print("------------------------")