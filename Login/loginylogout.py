import json
import os

# --------------------- RUTA FIJA DEL ARCHIVO JSON --------------------- #

# Obtiene la ruta real del archivo loginlogout.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Hace que usuarios.json SIEMPRE esté en la misma carpeta que loginlogout.py
RUTA_JSON = os.path.join(BASE_DIR, "usuarios.json")


# --------------------- MANEJO DEL ARCHIVO JSON --------------------- #

def cargar_usuarios():
    """
    Carga los usuarios desde usuarios.json.
    Si no existe, crea el archivo dentro de la carpeta Login.
    """
    if not os.path.exists(RUTA_JSON):
        with open(RUTA_JSON, "w", encoding="utf-8") as archivo:
            json.dump({}, archivo, indent=4)
        return {}

    with open(RUTA_JSON, "r", encoding="utf-8") as archivo:
        return json.load(archivo)


def guardar_usuarios():
    """
    Guarda el diccionario usuarios_registrados dentro de usuarios.json.
    """
    with open(RUTA_JSON, "w", encoding="utf-8") as archivo:
        json.dump(usuarios_registrados, archivo, indent=4)


# Cargar usuarios al iniciar
usuarios_registrados = cargar_usuarios()

# Usuario actual en sesión
usuario_actual = None


# --------------------- FUNCIONES PRINCIPALES --------------------- #

def login(username, password):
    global usuario_actual

    if not username or not password:
        return "Debes ingresar usuario y contraseña."

    if username not in usuarios_registrados:
        return "El usuario no existe."

    if usuarios_registrados[username] != password:
        return "Contraseña incorrecta."

    usuario_actual = username
    return f"Bienvenido, {username}. Iniciaste sesión correctamente."


def logout():
    global usuario_actual

    if usuario_actual is None:
        return "No hay ningún usuario conectado."

    nombre = usuario_actual
    usuario_actual = None
    return f"El usuario '{nombre}' cerró sesión correctamente."


def estado_sesion():
    if usuario_actual:
        return f"Usuario conectado: {usuario_actual}"
    return "No hay ningún usuario conectado."


def cambiar_contraseña():
    global usuario_actual

    if usuario_actual is None:
        return "Debes iniciar sesión para cambiar tu contraseña."

    contraseña_actual = input("Ingresa tu contraseña actual: ").strip()

    if usuarios_registrados[usuario_actual] != contraseña_actual:
        return "La contraseña actual no es correcta."

    nueva = input("Nueva contraseña: ").strip()
    confirmar = input("Confirma la nueva contraseña: ").strip()

    if not nueva:
        return "La nueva contraseña no puede estar vacía."

    if nueva != confirmar:
        return "Las contraseñas no coinciden."

    usuarios_registrados[usuario_actual] = nueva
    guardar_usuarios()  # Guardar cambios permanentemente

    return "La contraseña fue cambiada y guardada correctamente."


# --------------------- MENÚ INTERACTIVO --------------------- #

def menu():
    while True:
        print("\n----- MENÚ PRINCIPAL -----")
        print("1. Iniciar sesión")
        print("2. Cerrar sesión")
        print("3. Ver estado de sesión")
        print("4. Cambiar contraseña")
        print("5. Salir")

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            username = input("Usuario: ").strip()
            password = input("Contraseña: ").strip()
            print(login(username, password))

        elif opcion == "2":
            print(logout())

        elif opcion == "3":
            print(estado_sesion())

        elif opcion == "4":
            print(cambiar_contraseña())

        elif opcion == "5":
            print("Saliendo del sistema.")
            break

        else:
            print("Opción inválida. Intenta nuevamente.")


# Ejecutar menú
menu()