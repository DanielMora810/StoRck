#Busqueda de productos para el cajero
from .ManejodeInventario import Product
class Scanner:
    def iniciar_escaneo(self):
        while True:
            self.scan_product()
            x = input("¿Desea escanear otro producto? (si/no): ").strip().lower()
            if x == "no":
                break
            elif x != "si":
                print("Respuesta no válida.")
                break

    @staticmethod
    def scan_product():
        try:
            codigo = int(input("Escanee o ingrese el SKU del producto: "))
        except ValueError:
            print("El código debe de ser un número entero")
            return

        for producto in Product.lista_productos:
            if producto.sku == codigo:
                    print(f"Producto encontrado: {producto.name} - Precio: {producto.price}")
                    return

        print(" Producto NO registrado. No se puede procesar la venta.")
