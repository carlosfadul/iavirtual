frutas = ('naranja', 'manzana', 'pera', 'naranja', 'pera', 'banana')
frutas = tuple(('naranja', 'manzana', 'pera', 'naranja', 'pera', 'banana'))
lista = list(('naranja', 'manzana', 'pera', 'naranja', 'pera', 'banana'))
print(frutas.count('naranja'))
print(frutas.index('banana'))

print(len(frutas))

copia = list(frutas)
copia.remove("manzana")
print(copia)
frutas = tuple(copia)
print(frutas)
print(frutas[2:4])