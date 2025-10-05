#Conjuntos (set): Colección no ordenada de elementos únicos (no se puede acceder por índice)

frutas = {"manzana","naranja","mandarina", "naranja"}
print(type(frutas))
print(len(frutas))

# conjuntos = {"python",156,True}
# print(type(conjuntos))
# print(conjuntos)

# for item in conjuntos:
#     print(item)

print("manzana" in frutas)

#Agregar
#add
frutas.add("pera")
print(frutas)

#update
frutasTropicales = {"piña","mango"}
frutas.update(frutasTropicales) #agregar listas, tuplas, conjutos
print(frutas)

# Eleminarlos
frutas.remove("mango")
print(frutas)

# Discard
frutas.discard("pera")
print(frutas)

#Pop
frutas.pop() #Elimina un elemento aleatorio
print(frutas)

#clear
frutas.clear()
print(frutas)


print("----------------------")

a = {"a","b","c"}
b = {"c","d","e"}

c = a.union(b)
print(c)

i = a.intersection(b)
print(i)

d = a.difference(b)
print(d)