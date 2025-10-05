#Tuplas: colección ordenada e inmutable de elementos que permiten duplicados

tecnologias = ("python", "javascript","go")

print(tecnologias)
print(tecnologias[0])

print(len(tecnologias))

print(type(tecnologias))

fruta = ("manzana",)
print(type(fruta))

tupla = ("python",5,True)

x,y,z = tupla

tupla1 = (1,2,3)
tupla2 = (3,5,6)
tupla3 = tupla1+tupla2

print(tupla * 2)

for item in tupla:
    print(item)

print("--------------------")

tuplaAModificar = ("Python","javascript","go")
listaComodin = list(tuplaAModificar)
listaComodin.append("React")
tuplaAModificar = tuple(listaComodin)

print(tuplaAModificar)



