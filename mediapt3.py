nome=input(str("Nome: "))
ra=input(str("RA: "))
nota1=float(input("Digite sua primeira nota: "))
nota2=float(input("Digite sua segunda nota: "))
media1=(nota1+nota2)/2
print("Pedro Henrique Bonomo Santos, 1051392411015, Desenvolvimento de Software Multiplataforma")
while nota1 <0 or nota2 <0 or nota1 >10 or nota2 >10:
    print("Verifique se as notas são maiores que 0 e menores que 10")
    print("Tente novamente")
    nota1=float(input("Digite sua primeira nota: "))
    nota2=float(input("Digite sua segunda nota: "))
    media1=(nota1+nota2)/2
    print(f"Sua média é: {media1}")
    if media1>=7:
        print("Parabéns! Você está aprovado.")
    else:
        print(f"Você ainda tem uma chance {nome}! Estude para o próximo exame.")
print(f"Sua média é: {media1}")
if media1>=7:
        print(f"Parabéns {nome}! Você está aprovado.")
else:
        print(f"Você ainda tem uma chance, {nome}! Estude para o próximo exame.")
if media1>=7:
     exit()
terprova=str(input("Já fez a terceira prova? Escreva SIM ou NAO: "))
if terprova.lower()=="nao":
      print(f"Sinto muito, {nome}, volte quando tiver feito a terceira prova.")
      exit()
elif terprova.lower()=="sim":
      nota3=float(input(f"Boa sorte, {nome}! Digite sua nota: "))
media2=(media1+nota3)/2
print(media2)
while nota3 <0 or nota3 >10:
      print("Verifique se as notas são maiores ou iguais a 0 e menores ou iguais a 10.")
      print("Tente novamente")
      nota3=float(input("Digite sua nota: "))
      if media2>=5:
            print(f"Parabéns, {nome}, você aproveitou a sua chance! Está aprovado.")
      else:
        print(f"Sinto muito, {nome}, você não aproveitou sua chance. Estude mais para a próxima.")
if media2>=5:
      print(f"Parabéns, {nome}, você aproveitou a sua chance! Está aprovado.")
else:
      print(f"Sinto muito, {nome}, você não aproveitou sua chance. Estude mais para a próxima.")