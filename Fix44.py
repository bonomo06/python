import math
def cubo(x):
    return(x**3)
def fatorial(x):
    return math.factorial(x)
def divisao(x):
    return(x/9)
numero=int(input("Escolha um número: "))
print("Pedro Henrique Bonomo Santos, 1051392411015, Desenvolvimento de Software Multiplataforma")
if numero==1 or numero==2:
    print(cubo(numero))
elif numero%3==0:
    print(fatorial(numero))
elif numero==4 or numero==5 or numero==7 or numero==8:
    print(divisao(numero))
else:
    print("Valor inválido")