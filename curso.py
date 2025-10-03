with open("example1.txt", "w") as writefile:
    # aquí ya puedes escribir en el archivo
    writefile.write("Hola mundo desde Python!\n")

exam2 = 'example1.txt'
with open(exam2, 'r') as testread:
    print(testread.read())