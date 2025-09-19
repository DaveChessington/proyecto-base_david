from clases.avanzadas import Operaciones as op
calc=op()

calc.inputs(float(input("Numero 1:")),float(input("Numero 2:")))
calc.potencia()
print(calc.resultado)

calc.raiz()
print(calc.resultado)