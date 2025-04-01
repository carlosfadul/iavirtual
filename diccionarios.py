"""
carro = {
         "marca": "Ford",
         "modelo": "Mustang",
         "annio": "1964"
         }

#print(len(carro))
#print(carro["marca"])

hijos = {
            "hijo1": {
                    "nombre": "Emiliano",
                    "annio": 2006
                    },
            "hijo2": {
                    "nombre": "Valentina",
                    "annio": 2008,
                    "notas":[2.8,3.2,3.0]
                    }
            }

print(hijos["hijo2"]["nombre"])
print(hijos["hijo2"]["notas"][1])

carro = {
         "marca": "Ford",
         "modelo": "Mustang",
         "annio": "1964"    
         }
print(carro)
#carro.clear()
#print(carro)
vehiculo = carro.copy()
print(vehiculo)
print(carro.get("marca"))
print(carro.keys())
carro.pop("modelo")
print(carro)
carro.popitem()
print(carro)
carro.update({"modelo":"Fiesta"})
print(carro)
print(carro.values())

carro.setdefault("cilindraje","2500")
print(carro)
"""