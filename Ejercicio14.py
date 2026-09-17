class Potencias:
    @staticmethod
    def cuadrado(x):
        x2=x**2
        return x2
    @staticmethod
    def cubo(x):
        x3=x**3
        return x3

x=int(input("ingrese su numero"))
x2= Potencias.cuadrado(x)
x3= Potencias.cubo(x)

print(f"el cuadrado de tu numero es {x2} y el cubo es {x3}")