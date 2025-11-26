from .ManejodeInventario import Product
class Statics:
    def mostrar_reporte(self):
        self.most_sold()
        self.less_sold()

    @staticmethod
    def most_sold():
        if not Product.lista_productos:
            print("No hay productos registrados")
            return

        ordenados = sorted(Product.lista_productos, key=lambda p: p.sold, reverse=True)

        print("=== PRODUCTOS MÁS VENDIDOS ===")
        for producto in ordenados:
            print(f"{producto.name} - Vendidos: {producto.sold}")

    @staticmethod
    def less_sold():
        if not Product.lista_productos:
            print("No hay productos registrados")
            return

        ordenados = sorted(Product.lista_productos, key=lambda p: p.sold)

        print("\n=== PRODUCTOS MENOS VENDIDOS ===")
        for producto in ordenados:
            print(f"{producto.name} - Vendidos: {producto.sold}")
