# LISTAS: las listas son ordenadas, modificables y permiten valores duplicados

# frutas = ["manzana", "naranja", "mandarina"]
# print(type(frutas))

# frutas[1] = "banana"

# print(frutas)

# lista = ["edison",1,True]

# print(len(lista))

# print(frutas[0:2])

# if "manzana" in frutas:
#     print("la manzana esta dentro de las frutas")

vehiculos = ["Auto", "Moto", "Avión"]

#Metodos
# Append (agregar un elemento al final de la lista)

vehiculos.append("Barco")
print(vehiculos)

#Insert
vehiculos.insert(1, "bicicleta")
print(vehiculos)

# Remove
vehiculos.remove("Auto")
print(vehiculos)

# Pop
vehiculos.pop(1)
print(vehiculos)

#Sort
vehiculos.sort()
print(vehiculos)

#Reverse
vehiculos.reverse()
print(vehiculos)

#Unir listas
coleccion1 = [1,2,3]
coleccion2 = [4,5,6]

coleccion3 = coleccion1 + coleccion2
print(coleccion3)

coleccion1.extend(coleccion2)
print(coleccion1)