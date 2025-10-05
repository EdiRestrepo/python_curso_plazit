# Colecciones de pares clave valor (ordenado a partir de Python 3.7)

auto = {
    "marca": "renault",
    "modelo": "clio",
    "año": 2025
}

print(auto)
print(auto["marca"])
print(auto.get("marca"))

print(auto.keys())
print(auto.values())

if "marca" in auto:
    print("marca es una de las propiedades del diccionario")

auto["año"] = 2020

print(auto)

auto["color"] = "verde"
print(auto)

auto.update({"año":2024, "puertas":4})
print(auto)

# auto.pop("puertas")
# print(auto)

# auto.popitem() #Elimina el ultimo elemento del diccionario
# print(auto)

# auto.clear()
# print(auto)

for key in auto:
    print(key)

print("------------------")
for value in auto.values():
    print(value)

print("-----------------")
for key,value in auto.items():
    print(key, value)

#Diccionarios Anidados

familia = {
    "hijo1":{
        "nombre":"pedro",
        "edad":8
    },
     "hijo2":{
        "nombre":"juan",
        "edad":9
    },
     "hijo3":{
        "nombre":"ana",
        "edad":7
     }
}

print("------------------------")
print(familia["hijo1"]["nombre"])