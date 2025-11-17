from ManejodeInventario import Product

class Search:

    def buscar():

        while True:

            nombre = input("Ingrese el nombre del producto a buscar: ").lower()
        
            for producto in Product.lista_productos:
                if producto.name.lower() == nombre:
                    print("Producto encontrado")
                    print(producto)
                    return
                
                else:
                    print("El producto no existe en el sistema")

            x = input("¿Desea continuar?:")

            if x == "Si":
                continue

            elif x == "No":
                break

# Buscar producto
Search.buscar()

