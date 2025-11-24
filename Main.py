from Login.loginylogout import (
    login,
    logout,
    estado_sesion,
    cambiar_contraseña,
    registrar_usuario
)

def menu_principal():
    while True:
        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Iniciar sesión")
        print("2. Cerrar sesión")
        print("3. Estado de sesión")
        print("4. Cambiar contraseña")
        print("5. Registrar nuevo usuario")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

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

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida, intente de nuevo.")


# Ejecutar menú
menu_principal()