def adicao(x,y):
    return x+y
def subtrai(x,y):
    return x-y
def multi(x,y):
    return x*y
def divisao(x,y):
    return x/y       #nesse bloco eu mostrei as operações
n1=int(input("Digite o primeiro número: "))
n2=int(input("Digite o segundo número: "))
print("Escolha a operação")
print("1: Adição")
print("2: Subtração")
print("3: Multiplicação")
print("4: Divisão")
operacao=int(input(" "))    #nesse bloco eu mostrei as opções e falei pro usuario escolher a operação
print("Pedro Henrique Bonomo Santos, 1051392411015, Desenvolvimento de Software Multiplataforma")
if operacao==1:
        print("O resultado é: ", adicao(n1,n2))
elif operacao==2:
        print("O resultado é: ", subtrai(n1,n2))
elif operacao==3:
        print("O resultado é: ", multi(n1,n2))
elif operacao==4:
        print("O resultado é: ", divisao(n1,n2))
else:
        print("Escolha um número válido")