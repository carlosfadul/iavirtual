# Definimos una función llamada 'saludar' que toma un parámetro 'nombre'.
# Esta función imprime un mensaje de saludo personalizado.
def saludar(nombre):
    print(f"Hola, {nombre}! Bienvenido al programa.")

# Definimos una función llamada 'sumar' que toma dos parámetros 'a' y 'b'.
# Esta función devuelve la suma de los dos números.
def sumar(a, b):
    return a + b

# Definimos una función llamada 'menu' que no toma parámetros.
# Esta función muestra un menú de opciones al usuario y devuelve la opción seleccionada.
def menu():
    print("Menú de opciones:")
    print("1. Saludar")
    print("2. Sumar dos números")
    print("3. Salir")
    opcion = int(input("Seleccione una opción: "))
    return opcion

# Aquí comienza la ejecución principal del programa.
# Usamos un bucle while para mantener el programa en ejecución hasta que el usuario decida salir.
while True:
    # Llamamos a la función 'menu' para mostrar las opciones y obtener la selección del usuario.
    opcion = menu()

    # Verificamos qué opción seleccionó el usuario.
    if opcion == 1:
        # Si selecciona 1, pedimos un nombre y llamamos a la función 'saludar'.
        nombre = input("Ingrese su nombre: ")
        saludar(nombre)
    elif opcion == 2:
        # Si selecciona 2, pedimos dos números, los sumamos usando la función 'sumar' y mostramos el resultado.
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = sumar(num1, num2)
        print(f"La suma de {num1} y {num2} es {resultado}.")
    elif opcion == 3:
        # Si selecciona 3, salimos del bucle y terminamos el programa.
        print("Gracias por usar el programa. ¡Adiós!")
        break
    else:
        # Si elige una opción no válida, mostramos un mensaje de error.
        print("Opción no válida. Por favor, intente de nuevo.")