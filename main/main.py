import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Stock.ManejodeInventario import Product
from Stock.busquedadeproductos import Search
from Stock.busquedadeproductos_cajero import Scanner
from Stock.consultasdeBodega import WarehouseChief
from Stock.productosmásymenosvendidos import Statics

class MenuPrincipal:
    @staticmethod
    def mostrar_main():
        """Muestra las opciones del menú principal."""
        print("\n" + "="*40)
        print("       MENÚ PRINCIPAL - TIENDA")
        print("="*40)
        print("1. Gestión de Inventario")
        print("2. Gestión de Bodega")
        print("3. Búsqueda de producto (Administrador)")
        print("4. Búsqueda de producto (Cajero/Escaner)")
        print("5. Productos más y menos vendidos")
        print("6. Salir")
        print("="*40)

    @staticmethod
    def menu_interactivo():
        """Bucle principal del programa."""
        while True:
            MenuPrincipal.mostrar_main()
            opt = input("\nIngrese una opción (1-6): ").strip()

            match opt:
                case '1':
                    print("\n>> MÓDULO: Gestión de Inventario")
                    # Aquí instancias el menú o ejecutas la lógica del módulo
                    producto = Product()  # ¡Importante: instanciar con ()!
                    producto.menu_gestion()  # Suponiendo que la clase tiene un método así

                case '2':
                    print("\n>> MÓDULO: Gestión de Bodega")
                    jefe_bodega = WarehouseChief()
                    jefe_bodega.menu_principal()  # Método típico en este tipo de clases

                case '3':
                    print("\n>> MÓDULO: Búsqueda de producto (Administrador)")
                    buscador = Search()
                    buscador.iniciar_busqueda()  # o el método que tenga para buscar

                case '4':
                    print("\n>> MÓDULO: Escáner para Cajero")
                    escaner = Scanner()
                    escaner.iniciar_escaneo()  # Método común en módulos de cajero

                case '5':
                    print("\n>> ESTADÍSTICAS: Productos más y menos vendidos")
                    stats = Statics()
                    stats.mostrar_reporte()  # o mostrar_estadisticas(), etc.

                case '6':
                    print("\n¡Gracias por usar el sistema! Hasta luego")
                    break

                case _:
                    print("Opción no válida. Por favor, elija del 1 al 6.")
                    input("Presione Enter para continuar...")

if __name__ == "__main__":
    MenuPrincipal.menu_interactivo()