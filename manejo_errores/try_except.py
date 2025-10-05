try:
    print("intento ejecutar este codigo")
    x = 5 / 0
    print(x)
except ZeroDivisionError as e:
    print("Ocurrió un error:","No se puede dividir entre cero",e)

try:
    print(x)
except NameError as e:
    print("Ocurrió un error:","La variable x no está definida",e)
finally:
    print("Esto se ejecuta siempre, haya o no error")