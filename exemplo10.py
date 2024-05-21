# Meu 1ro programa em Python
rato= input("Qual sua idade? ") #o input habilita o teclado
print("Essa é sua idade= "+ rato) #o print é para mostrar ao usuario
type(rato) #o type vai apenas mostrar o tipo. Ex: string
print(type(rato))
nome="12"
idade="robsin" #colocar a palavra e depois o "=", você mostrou que existe, é uma variavel
print(nome,idade) #vai aparecer 12 robsin, pois eu mostrei que nome é 12 e idade é robsin
sujeito="Python"
verbo="é"
adjetivo="legal"
print(sujeito,verbo,adjetivo)
login=input("Login= ")
senha= int(input("Senha= ")) #precisa colocar o int para falar que não é string e sim inteiro
print("O usuario digirou o login:%s e a senha:%s" %(login, senha)) 
#toda variavel começa com letra
if senha==129810:
    print("Acesso permitido") #necessário dar o tab para saber que é dentro do if e do else
else:
    print("Acesso negado")
num1=int(4)
num2=int(5) #devo colocar o int para ele identificar como numero inteiro e nao como string
num3=num1+num2
print(num3)
print(type(num3))