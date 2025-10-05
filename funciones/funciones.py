#Función: bloque de código que solo se ejecuta cuando lo llamamos. Permite organizar y modularizar el código (reutilización)

def mi_funcion():
    print("hola mundo")

mi_funcion()

print("---------------")
def saludar(nombre): #Argumentos
    print("Hola", nombre)

saludar("pedro") #Parametros

print("---------------")
def saludar2(nombre, apellido="restrepo"):
    print("Hola", nombre, apellido)

saludar2("Maria")

print("---------------")
def sumar(a,b):
    return a+b

print(sumar(2,3))

def funcion():
    pass
