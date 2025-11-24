from datetime import datetime, timedelta
from .ManejodeInventario import Product

class WarehouseChief:

    def menu_principal(self):
        while True:
            print("\n=== CONSULTAS DE BODEGA ===")
            print("1. Ver productos próximos a vencer")
            print("2. Volver al menú principal")
            opcion = input("Seleccione una opción: ").strip()
            if opcion == '1':
                self.near_expiration()
            elif opcion == '2':
                break
            else:
                print("Opción no válida.")

    @staticmethod
    def near_expiration(days = 30):

        if not Product.lista_productos:
            print("No hay productos registrados")
            return

        hoy = datetime.now()
        limite = hoy + timedelta(days = days)

        proximos = [
            p for p in Product.lista_productos
            if hasattr(p, 'expiration_date') and p.expiration_date and p.expiration_date <= limite
        ]

        if not proximos:
            print(f"No hay productos que venzan en los próximos {days} días.")
            return

        print(f"=== PRODUCTOS PRÓXIMOS A VENCER (≤ {days} días) ===")
        for p in proximos:
            dias_restantes = (p.expiration_date - hoy).days
            print(f"{p.name} - Vence en {dias_restantes} días")