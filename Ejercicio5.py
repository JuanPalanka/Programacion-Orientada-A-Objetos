class Operaciones:
    @staticmethod
    def Op1(suma,x):
        suma=suma+x
        return suma
    @staticmethod
    def op2(x,y):
        x=x+(y**2)
        return x
    @staticmethod
    def op3(suma,x,y):
        suma=suma+(x/y)
        return suma


suma=int(input("Ingrese el valor de Suma "))
x=int(input("Ingrese el valor de x "))
y=int(input("Ingrese el valor de y "))

suma= Operaciones.Op1(suma,x)
x=Operaciones.op2(x,y)
suma=Operaciones.op3(suma,x,y)

print(f"El valor de la suma es {suma}")
