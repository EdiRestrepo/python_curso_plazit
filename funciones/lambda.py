#Lambda es una funcion pequeña y anónima que puede tener muchos argumentos pero sólo una expresion

#Sintaxis lambda argumentos : expresión

# x = lambda a, b : a + b

# print(x(5,3))

def mifuncion(n):
    return lambda a : a * n

duplicador = mifuncion(2)
triplicador = mifuncion(3)

print(duplicador(5))
print(triplicador(5))