# ----- Sistema de Login / Logout Provisional -----

usuarios_registrados = {
    "johann": "1234",
    "admin": "admin"
}

usuario_actual = None


def login(username, password):
    global usuario_actual

    if username in usuarios_registrados:
        if usuarios_registrados[username] == password:
            usuario_actual = username
            return f"Bienvenido, {username}. Iniciaste sesión correctamente."
        else:
            return "Contraseña incorrecta."
    else:
        return "El usuario no existe."


def logout():
    global usuario_actual

    if usuario_actual is None:
        return "No hay ningún usuario conectado."

    usuario_desconectado = usuario_actual
    usuario_actual = None
    return f"El usuario '{usuario_desconectado}' cerró sesión."


def estado_sesion():
    if usuario_actual:
        return f"Usuario conectado: {usuario_actual}"
    else:
        return "No hay ningún usuario conectado."


# ----- Menú interactivo -----

def menu():
    while True:
        print("\n----- MENÚ -----")
        print("1. Iniciar sesión")
        print("2. Cerrar sesión")
        print("3. Ver estado de sesión")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            username = input("Usuario: ")
            password = input("Contraseña: ")
            print(login(username, password))

        elif opcion == "2":
            print(logout())

        elif opcion == "3":
            print(estado_sesion())

        elif opcion == "4":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")


# Llamar al menú para iniciar
menu()