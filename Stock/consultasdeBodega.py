from datetime import datetime, timedelta
from ManejodeInventario import Product

class WarehouseChief:

    @staticmethod
    def near_expiration(days = 30):
        
        if not Product.lista_productos:
            print("No hay productos registrados")
            return
        
        hoy = datetime.now()
        limite = hoy + timedelta(days = days)

        proximos = [
            p for p in Product.lista_productos 
            if p.expiration_date <= limite
        ]

        if not proximos:
            print(f"No hay productos que venzan en los próximos {days} días.")
            return

        print(f"=== PRODUCTOS PRÓXIMOS A VENCER (≤ {days} días) ===")
        for p in proximos:
            dias_restantes = (p.expiration_date - hoy).days
            print(f"{p.name} - Vence en {dias_restantes} días")