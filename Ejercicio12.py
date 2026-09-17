class Pagos:
    @staticmethod
    def salariobruto(horas, valorhora):
        salariobruto=horas*valorhora
        return salariobruto
    @staticmethod
    def retefuente(salariobruto):
        retefuente= salariobruto*0.125
        return retefuente
    @staticmethod
    def salarioneto(salariobruto, retefuente):
        salarioneto=salariobruto-retefuente
        return salarioneto

horas=int(input("Ingrese las horas trabajadas"))
valorhora=int(input("Ingrese el valor pagado por hora"))
salariobruto= Pagos.salariobruto(horas, valorhora)
retefuente= Pagos.retefuente(salariobruto)
salarioneto= Pagos.salarioneto(salariobruto, retefuente)

print(f"Salario bruto: {salariobruto}$, Retefuente: {retefuente}$, Salario neto: {salarioneto}$")