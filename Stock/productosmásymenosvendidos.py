from ManejodeInventario import Product
class Statics:
    @staticmethod
    
    def most_sold():
        if not Product.lista_productos:
            print("No hay productos registrados")
            return


        ordenados = sorted(Product.lista_productos, key=lambda p: p.sold, reverse=True)

        print("===Productos más vendidos===")
        for producto in ordenados:
            print(f"{producto.name} - Vendidos: {producto.sold}")


   # def get_sold(productos):
       # return productos.sold


#ordenados = sorted(Product.lista_productos, key= get_sold(), reverse=True)

    @staticmethod

    def less_sold():
        
        if not Product.lista_productos:
            print("No hay productos registrados")
            return
        
        ordenados = sorted(Product.lista_productos, key=lambda p: p.sold)

        print("\n=== PRODUCTOS MENOS VENDIDOS ===")
        for producto in ordenados:
            print(f"{producto.name} - Vendidos: {producto.sold}")


Statics.most_sold()
Statics.less_sold()
