class Product:

    lista_productos = []

    def __init__(self, sku = None, name = None, cost = None, price = None, stock = None , cost_dozen = None, sold = None, expiration_date = None):
        self.sku = sku
        self.name = name
        self.cost = cost
        self.price = price
        self.stock = stock
        self.cost_dozen = cost_dozen
        self.sold = sold
        self.expiration_date = expiration_date


        

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

    def menu_gestion(self):
        """Método para gestionar el inventario."""
        while True:
            print("\n=== GESTIÓN DE INVENTARIO ===")
            print("1. Agregar producto")
            print("2. Mostrar productos")
            print("3. Volver al menú principal")
            opcion = input("Seleccione una opción: ").strip()
            if opcion == '1':
                self.add_product()
            elif opcion == '2':
                Product.show_products()
            elif opcion == '3':
                break
            else:
                print("Opción no válida.")