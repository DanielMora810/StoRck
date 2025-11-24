import json
import os

# --------------------- RUTA DEL ARCHIVO JSON --------------------- #

BASE_DIR = os.path.dirname(os.path.abspath(__file__))   # Carpeta Login
RUTA_JSON = os.path.join(BASE_DIR, "usuarios.json")     # Archivo dentro de Login


# --------------------- MANEJO DEL ARCHIVO JSON --------------------- #

def cargar_usuarios():
    if not os.path.exists(RUTA_JSON):
        # Crear archivo vacío si no existe
        with open(RUTA_JSON, "w", encoding="utf-8") as archivo:
            json.dump({}, archivo, indent=4, ensure_ascii=False)
        return {}

    # Leer archivo existente
    with open(RUTA_JSON, "r", encoding="utf-8") as archivo:
        return json.load(archivo)


def guardar_usuarios():
    with open(RUTA_JSON, "w", encoding="utf-8") as archivo:
        json.dump(usuarios_registrados, archivo, indent=4, ensure_ascii=False)


usuarios_registrados = cargar_usuarios()
usuario_actual = None


# --------------------- FUNCIONES PRINCIPALES --------------------- #

def registrar_usuario():
    print("\n=== REGISTRAR NUEVO USUARIO ===")
    username = input("Ingrese nuevo nombre de usuario: ")

    if not username:
        return "El nombre de usuario no puede estar vacío."

    if username in usuarios_registrados:
        return "Ese usuario ya existe."

    password = input("Ingrese contraseña: ")
    confirmar = input("Confirme la contraseña: ")

    if not password:
        return "La contraseña no puede estar vacía."

    if password != confirmar:
        return "Las contraseñas no coinciden."

    usuarios_registrados[username] = password
    guardar_usuarios()
    return f"Usuario '{username}' registrado correctamente."


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
    return "No hay ninguna sesión activa."


def cambiar_contraseña():
    global usuario_actual

    if usuario_actual is None:
        return "Debes iniciar sesión para cambiar tu contraseña."

    actual = input("Ingresa tu contraseña actual: ")

    if usuarios_registrados[usuario_actual] != actual:
        return "La contraseña actual no es correcta."

    nueva = input("Nueva contraseña: ")
    confirmar = input("Confirma la nueva contraseña: ")

    if not nueva:
        return "La contraseña no puede estar vacía."

    if nueva != confirmar:
        return "Las contraseñas no coinciden."

    usuarios_registrados[usuario_actual] = nueva
    guardar_usuarios()

    return "La contraseña fue cambiada correctamente."