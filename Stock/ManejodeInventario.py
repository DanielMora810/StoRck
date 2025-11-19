class Product:

    lista_productos = []

    def __init__(self, sku = None, name = None, cost = None, price = None, stock = None , cost_dozen = None, sold = None):
        self.sku = sku
        self.name = name
        self.cost = cost
        self.price = price
        self.stock = stock
        self.cost_dozen = cost_dozen
        self.sold = sold



    def add_product(self):
        
        self.sku = int(input("Ingresar código de identificación: "))
        self.name = input("Ingresar nombre del producto: ")
        self.cost = int(input("Ingresar costo de compra del producto: "))
        self.price = int(input("Ingresar el precio de venta al público: "))
        self.cost_dozen = int(input("Ingresar precio al público por docena: "))
        self.sold = int(input("Ingrese cuántas unidades se han vendido: "))


        Product.lista_productos.append(self)


    def __str__(self):
        return f"SKU: {self.sku}, Nombre: {self.name}, Costo: {self.cost}, Precio: {self.price}, Docena: {self.cost_dozen}"
    
    @classmethod

    def show_products(cls):
        print("\n=== LISTA DE PRODUCTOS ===")
        for i, producto in enumerate(cls.lista_productos, 1):
            print(f"{i}. {producto}")


while True:
    producto1 = Product()
    producto1.add_product()

    x = input("¿Desea continuar? (si/no): ")
    if x.lower() == "no":
        break
    elif x.lower() == "si":
        continue

# Imprimir todos los productos

Product.show_products()