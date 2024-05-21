salario=float(input("Digite seu sálario: "))
aumento1=salario*1.20
aumento2=salario*1.10
aumento3=salario*1.05
print("Pedro Henrique Bonomo Santos, 1051392411015, Desenvolvimento de Software Multiplataforma")
if salario<=1500:
    print(aumento1)
elif salario >1500 and salario <2500:
    print(aumento2)
else:
    print(aumento3)