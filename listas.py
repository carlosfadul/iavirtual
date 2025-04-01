"""
frutas = ["naranja","papaya","manzana","piña"]

print(len(frutas)) 
print(frutas[1:3])
print(frutas[-1][1])

frutas = ["naranja","papaya","manzana","piña"]
print(frutas)
frutas.append("uva")
print(frutas)

frutas.clear()
print(frutas)

frutas2 = frutas.copy()
print(frutas2)

frutas3 = frutas
print(frutas3)
frutas3.append("kiwi")
print(frutas3)  

print(frutas)

print(frutas2)
frutas2.append("chontaduro")
print(frutas2)
print(frutas)

frutas = ["naranja","papaya","manzana","naranja","piña"]
print(frutas)
conteo = frutas.count("naranja")
print(conteo)
print(frutas.count("naranja"))
fruticas = ["uva","kiwi","chontaduro"]
frutas.extend(fruticas)
print(frutas)
print(frutas.index("piña"))
print(frutas.index("naranja"))
frutas.insert(2,"banano")
print(frutas)
print(frutas.pop())
print(frutas.pop(3))

print(frutas)
frutas.remove("naranja")
print(frutas)
#frutas.remove("chontaduro")
frutas.reverse()
print(frutas)
frutas.sort()
print(frutas)

numeros = [5,8,3,1,7,6,2,4]
numeros.sort()
print(numeros)
"""