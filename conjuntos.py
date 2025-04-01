"""
frutas = {"manzana", "naranja", "pera", "manzana", "naranja", "pera"}
print(frutas) # {'naranja', 'manzana', 'pera'}
print(len(frutas))
frutas.add("uva")
print(frutas)
copia = frutas.copy()
copia.add("kiwi")
print(copia)

frutas = {"manzana", "naranja", "pera", "manzana", "naranja", "pera"}
carros = {"ford", "chevrolet", "pera", "ford", "chevrolet", "mazda"}
print(frutas.difference(carros))
print(frutas.intersection(carros))
print(frutas.union(carros))
frutas.discard("kiwi")
print(frutas)

#frutas.remove("kiwi")
#print(frutas)

#frutas.clear()
print(frutas) 

colores = {"rojo", "verde", "azul"}
otros_colores = {"rojo", "verde"}
print(colores.issubset(otros_colores))
print(otros_colores.issubset(colores))

print(colores.issuperset(otros_colores))
print(otros_colores.issuperset(colores))

""" 
