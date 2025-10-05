# open(nombre, modo de apertura r,w,a,x,a,r+)

# r: read (lectura) - valor por defecto. Abre el archivo para lectura, error si no existe
# w: write (escritura) - crea un archivo nuevo o sobrescribe uno existente
# a: append (adicionar) - agrega contenido al final del archivo, crea uno nuevo si no existe
# x: exclusive creation (creación exclusiva) - crea un archivo nuevo, error si ya existe
# r+: read and write (lectura y escritura) - abre el archivo para lectura y escritura
# with open("example1.txt", "w") as writefile:
#     # aquí ya puedes escribir en el archivo   
#     writefile.write("Hola mundo desde Python!\n")
#     writefile.write("Segunda linea\n")
#     writefile.write("Tercera linea\n")
#     writefile.write("Cuarta linea\n") 

# try:
#     f = open("archivo.txt", "r")
#     print(f.readline())
#     f.close()
# except FileNotFoundError as e:
#     print("Ocurrió un error:", "El archivo no fue encontrado", e)

try:
    with open("archivo.txt", "r", encoding="utf-8") as f:
        print(f.readline())
        print(f.readline())
except FileNotFoundError as e:
    open("archivo.txt","x",encoding="utf-8")
    print("Ocurrió un error:", "El archivo no fue encontrado", e)

try:
    with open("archivo.txt", "a", encoding="utf-8") as f:
        f.write("Escribiendo en el archivo...\n")
        f.write("Segunda línea\n")
        f.write("Tercera línea\n")
    with open("archivo.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError as e:
    print("Ocurrió un error:", "El archivo no fue encontrado", e)
