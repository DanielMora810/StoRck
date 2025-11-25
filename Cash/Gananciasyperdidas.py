import json
import os
from datetime import datetime

AR = "registro.json"    

# MODULO DE CASH

registros = {}   


#APARTADO DE JSON

def cargar_registros():
    global registros
    if os.path.exists(AR):
        with open(AR, "r") as f:
            registros = json.load(f)
            print("Registros cargados.")
    else:
        print("No hay registros.")
        registros = {}
def guardar_registros():
    with open(AR, "w") as f:
        json.dump(registros, f)
        print("Registros guardados.")




def registro_gana():
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

    guardar_registros()
    print(f"Ganancia registrada en la fecha {dia} a las {hora}.")


def registro_pierde():
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
    
    guardar_registros()
    print(f"Pérdida registrada en la fecha {dia} a las {hora}.")


def seleccion_dia():
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
    dia = seleccion_dia()
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

        
def filtro_rangofecha():
    if not registros:
        print("No hay registros todavía.")
        return
    
    fecha_inicio = input("Ingrese fecha de inicio (dd/mm/aaaa): ")
    fecha_fin = input("Ingrese fecha final (dd/mm/aaaa): ")

    try:
        inicio = datetime.strptime(fecha_inicio, "%d-%m-%Y")
        fin = datetime.strptime(fecha_fin, "%d-%m-%Y")
    except ValueError:
        print("Formato de fecha inválido.")
        return

    print("\n--- REGISTROS EN EL RANGO ---")
    encontrados = False

    for dia in registros:
        fecha_dia = datetime.strptime(dia, "%d-%m-%Y")

        if inicio <= fecha_dia <= fin:
            encontrados = True
            datos = registros[dia]

            total_g = sum(a["monto"] for a in datos["ganancias"])
            total_p = sum(a["monto"] for a in datos["perdidas"])

            print(f"\nDía: {dia}")
            print("Ganancias:", total_g)
            print("Pérdidas:", total_p)
            print("Balance:", total_g - total_p)

    if not encontrados:
        print("No se encontraron registros en este rango de fechas.")
        
""""       
def menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Registrar ganancia")
        print("2. Registrar pérdida")
        print("3. Mostrar resumen por día")
        print("4. Filtrar por rango de fechas")
        print("5. Salir")

        op = input("Seleccione una opción: ")

        if op == "1":
            registro_gana()
        elif op == "2":
            registro_pierde()
        elif op == "3":
            mostrar_resumen()
        elif op == "4":
            filtro_rangofecha()
        elif op == "5":
            print("Guardando datos antes de salir...")
            guardar_registros()
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida, intente de nuevo.")

cargar_registros()
menu()
"""
    