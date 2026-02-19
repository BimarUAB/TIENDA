# CLASE PRODUCTO
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Precio: ${self.precio}")
        print(f"Cantidad: {self.cantidad}")
        print("-" * 20)
    
    def valor_total(self):
        return self.precio * self.cantidad


# LISTA VACÍA PARA GUARDAR PRODUCTOS
lista_productos = []


# FUNCIÓN PARA AGREGAR PRODUCTO
def agregar_producto():
    print("\n--- AGREGAR PRODUCTO ---")
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio: "))
    cantidad = int(input("Ingrese la cantidad: "))
    
    # Crear objeto Producto
    nuevo_producto = Producto(nombre, precio, cantidad)
    
    # Guardar en la lista
    lista_productos.append(nuevo_producto)
    print("✓ Producto agregado exitosamente!\n")


# FUNCIÓN PARA MOSTRAR PRODUCTOS
def mostrar_productos():
    print("\n--- LISTA DE PRODUCTOS ---")
    if len(lista_productos) == 0:
        print("No hay productos registrados.")
    else:
        for producto in lista_productos:
            producto.mostrar_info()
            print(f"Valor total en stock: ${producto.valor_total()}")
            print("=" * 20)
    print()


# MENÚ INTERACTIVO
while True:
    print("===== MENÚ =====")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        mostrar_productos()
    elif opcion == "3":
        print("¡Hasta luego!")
        break  # Sale del bucle while
    else:
        print("Opción no válida. Intente de nuevo.\n")