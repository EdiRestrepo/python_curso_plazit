# with open("example1.txt", "w") as writefile:
#     # aquí ya puedes escribir en el archivo
#     writefile.write("Hola mundo desde Python!\n")

# exam2 = 'example1.txt'
# with open(exam2, 'r') as testread:
#     print(testread.read())

# A='1234567'
# print(A[1::2])

# Name="Michael Jackson" 
# print(Name.find('el'))
# A=((11,12),[21,22])

# print(A[1])
# def Add(x,y):
#     z=y+x
#     return(y)

# print(Add('1','1'))

class Points(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def print_point(self):
        print('x=',self.x,'y=',self.y)

point =Points(1,2)

print(point.print_point())