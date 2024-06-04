def calcular_pagamento(x,y):
    return x*y
def calcular_horasextra(x,y):
    horas_extras= x-40
    pagamento_normal= x*y
    pagamento_extra=horas_extras * y
    return pagamento_normal+pagamento_extra
horas=int(input("Digite suas horas trabalhadas na semana: "))
valor=float(input("Digite o valor/hora: "))
print("Pedro Henrique Bonomo Santos RA:1051392411015 Desenvolvimento de Software Multiplataforma")
if horas<=40:
    print(calcular_pagamento(valor,horas))
elif horas>40:
    print(calcular_horasextra(horas,valor))