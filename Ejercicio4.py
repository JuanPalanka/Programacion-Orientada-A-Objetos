class Edades:
    @staticmethod
    def edalberto(edjuan):
        edalberto=(edjuan*2)/3
        return edalberto
    @staticmethod
    def edana(edjuan):
        edana=(edjuan*4)/3
        return edana
    @staticmethod
    def edmama(edjuan,edalberto,edana):
        edmama=edjuan+edalberto+edana
        return edmama

edjuan=int(input("Ingrese la edad de juan"))
edalberto=Edades.edalberto(edjuan)
edana= Edades.edana(edjuan)
edmama= Edades.edmama(edjuan, edalberto, edana)

print(f"Las edades son: edad de la mama: {edmama}, edad de juan: {edjuan}, edad de alberto {edalberto}, edad de ana: {edana}")
