def numero_positivo(x):
    return(abs(x))
def maior_10(x,y):
    return(x-y)
def numero_5(x):
    return(x/5)
valor1=float(input("Digite um número: "))
valor2=float
print("Pedro Henrique Bonomo Santos, 1051392411015, Desenvolvimento de Software Multiplataforma")
if valor1<0:
    print(numero_positivo(valor1))
elif valor1>10:
    print("Escolha outro valor")
    valor2=float(input(""))
    print(maior_10(valor1,valor2))
else:
    print(numero_5(valor1))