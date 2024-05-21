def aumento1(x):
    return(x*1.20)
def aumento2(x):
    return(x*1.10)
def aumento3(x):
    return(x*1.05)
salario=float(input("Digite seu sálario: "))
print("Pedro Henrique Bonomo Santos, 1051392411015, Desenvolvimento de Software Multiplataforma")
if salario<=1500:
    print(aumento1(salario))
elif salario >1500 and salario <2500:
    print(aumento2(salario))
else:
    print(aumento3(salario))