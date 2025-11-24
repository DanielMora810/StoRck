from .ManejodeInventario import Product

class Search:

    def iniciar_busqueda(self):
        while True:
            nombre = input("Ingrese el nombre del producto a buscar: ").lower()

            encontrado = False
            for producto in Product.lista_productos:
                if producto.name.lower() == nombre:
                    print("Producto encontrado")
                    print(producto)
                    encontrado = True
                    break

            if not encontrado:
                print("El producto no existe en el sistema")

            x = input("¿Desea continuar? (Si/No): ").strip().lower()

            if x == "no":
                break
            elif x != "si":
                print("Respuesta no válida. Asumiendo no.")
                break

