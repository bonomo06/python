def salario1(x):
    return x*1.20
def salario2(x):
    return x*1.10
def salario3(x):
    return x*1.05
salario=int(input("Digite seu sálario: "))
print("Pedro Henrique Bonomo Santos, 1051392411015, Desenvolvimento de Software Multiplataforma")
if salario <=1500:
    print(f"Esse é seu antigo sálario: {salario}")
    print(f"Esse é seu novo sálario: {salario1(salario)}")
elif salario >1500 and salario < 2500:
    print(f"Esse é seu antigo sálario: {salario}")
    print(f"Esse é seu novo sálario: {salario2(salario)}")
else:
    print(f"Esse é seu antigo sálario: {salario}")
    print(f"Esse é seu novo sálario: {salario3(salario)}")