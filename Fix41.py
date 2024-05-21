import math
def elevado(x):
    return x**2
def raiz(x):
    return (math.sqrt(x))
def divisao(x):
    return x/9
valor=int(input("Escolha um número entre 1 e 9 sem ser o 5: "))
print("Pedro Henrique Bonomo Santos, 1051392411015, Desenvolvimento de Software Multiplataforma")
if valor>=1 and valor<=3:
    print(elevado(valor))
elif valor==4 or valor==9:
    print(raiz(valor))
elif valor>=6 and valor<=8:
    print(divisao(valor))
while valor==5 or valor>9 or valor<1:
    print("Por favor, escolha um número entre 1 e 9, menos o número 5: ")
    valor=int(input("Escolha um número entre 1 e 9 sem ser o 5: "))
    if valor>=1 and valor<=3:
        print(elevado(valor))
    elif valor==4 or valor==9:
        print(raiz(valor))
    elif valor>=6 and valor<=8:
        print(divisao(valor))