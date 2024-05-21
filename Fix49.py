nome=str(input("Digite seu nome "))
idade=int(input("Digite sua idade "))
print("Pedro Henrique Bonomo Santos, 1051392411015, Desenvolvimento de Software Multiplataforma")
if idade>=18 and idade<64:
    print(f"Bem vindo, {nome}, você é maior de idade")
elif idade<18 and idade>0:
    print(f"Bem vindo, {nome}, você é menor de idade")
elif idade>=65:
    print(f"Bem vindo, {nome}, você é maior de 65 anos")