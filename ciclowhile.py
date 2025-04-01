"""
tabla = int(input("Ingrese la tabla de multiplicar: "))
i = 1
while i <= 10:
    print(tabla, "*", i, "=", i*tabla)
    i += 1

frutas = ["manzana", "naranja", "pera", "papaya", "aguacate", "fresa"]
tamano = len(frutas)
#print("El tamaño de la lista es: ", tamano)
i = 0
while i < tamano:
    print(frutas[i])
    i += 1
"""

#productos = []
bandera = True
while bandera:
    print("1. Agregar producto")
    print("2. Buscar producto")
    print("3. Mostrar todos los productos")
    print("4. Salir")
    opcion = int(input("Ingrese una opción: "))
    if opcion == 1:
        producto = input("Ingrese el nombre del producto: ")
        #productos.append(producto)
        print("Producto agregado")
    elif opcion == 2:
        #
        print("pepito")
        #
    elif opcion == 4:
        bandera = False
    else:
        print("Opción no válida")
print("Fin del programa")