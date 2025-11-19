#Busqueda de productos para el cajero
from ManejodeInventario import Product
class Scanner:
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
