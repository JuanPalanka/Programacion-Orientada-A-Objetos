import math

class Circulo:
    @staticmethod
    def area(radio):
        area= math.pi*(radio**2)
        return area
    @staticmethod
    def longitud(radio):
        longitud= 2*math.pi*radio
        return longitud

radio= float(input("Ingrese el radio de la circunferencia"))
area= Circulo.area(radio)
longitud= Circulo.longitud(radio)

print(f"El area del circulo es: {area}, y la longitud es: {longitud}")