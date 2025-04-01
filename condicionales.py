"""
edad = int(input("Introduce tu edad: "))
if edad >= 18:
    print("Eres mayor de edad")
    print("puedes ver películas para adultos")
    print("puedes comprar cerveza")
else:
    print("Eres menor de edad")
    print("no puedes ver películas para adultos")
    print("no puedes comprar cerveza")
print("Aquí ya esta instrucción no depende de nadie")
print("Fin del programa")

edad = int(input("Introduce tu edad: "))
if edad >= 0 and edad <6:
    print("primera infancia")
elif edad >= 6 and edad <12:
    print("infancia")
elif edad >= 12 and edad <18:
    print("Adolescente")
elif edad >= 18 and edad <26:
    print("Adulto joven")
    print("Está en una edad muy chévere")
elif edad >= 26 and edad <60:
    print("Adulto")
elif edad >= 60 and edad < 130:
    print("Adulto mayor")
else:
    print("Edad incorrecta")

# primera infancia entre 0 y 6
# infancia entre 6 y 12
# adolcentes entre 12 y 18
# adultos jovenes entre 18 y 26
# adultos entre 26 y 60
# adultos mayores de 60 en adelante
"""
# Pedir un número al usuario y decir el día de la semana de acuerdo al número
# 1 - lunes
# 2 - martes    