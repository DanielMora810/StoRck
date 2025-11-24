from Login.loginylogout import (
    login,
    logout,
    estado_sesion,
    cambiar_contraseña,
    registrar_usuario
)


# --- Cash ---
from Cash.Gananciasyperdidas import (
    cargar_registros,
    registro_gana,
    registro_pierde,
    mostrar_resumen,
    filtro_rangofecha
)

# cargar registros de cash al iniciar
cargar_registros()


# ==============================
#      MENÚ PRINCIPAL
# ==============================

def menu_principal():
    while True:
        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Iniciar sesión")
        print("2. Cerrar sesión")
        print("3. Estado de sesión")
        print("4. Cambiar contraseña")
        print("5. Registrar usuario nuevo")
        print("6. Registrar Ganancias")
        print("7. Registrar Perdidas")
        print("8. Mostrar resumen del día")
        print("9. Filtrar por rango de fechas")
        print("10. Salir")

        opcion = input("Seleccione una opción: ")

        # ------ LOGIN ------
        if opcion == "1":
            usuario = input("Usuario: ")
            contraseña = input("Contraseña: ")
            print(login(usuario, contraseña))

        elif opcion == "2":
            print(logout())

        elif opcion == "3":
            print(estado_sesion())

        elif opcion == "4":
            print(cambiar_contraseña())

        elif opcion == "5":
            print(registrar_usuario())

        # ------ CASH ------
        elif opcion == "6":
            registro_gana()

        elif opcion == "7":
            registro_pierde()

        elif opcion == "8":
            mostrar_resumen()

        elif opcion == "9":
            filtro_rangofecha()

        # ------ SALIDA ------
        elif opcion == "10":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida, intente de nuevo.")


# Iniciar programa
menu_principal()