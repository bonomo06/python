def media(x,y):
    return(x+y)/2
nome=input(str("Nome: "))
ra=input(str("RA: "))
nota1=float(input("Digite sua primeira nota: "))
nota2=float(input("Digite sua segunda nota: "))
media1_total=media(nota1,nota2)
print("Pedro Henrique Bonomo Santos, 1051392411015, Desenvolvimento de Software Multiplataforma")
print(f"Sua média é: {media1_total}")
if media1_total>=7:
        print(f"Parabéns {nome}! Você está aprovado.")
else:
        print(f"Você ainda tem uma chance, {nome}! Estude para o próximo exame.")
if media1_total>=7:
     exit()
terprova=str(input("Já fez a terceira prova? Escreva SIM ou NAO: "))
if terprova.lower()=="nao":
      print(f"Sinto muito, {nome}, volte quando tiver feito a terceira prova.")
      exit()
elif terprova.lower()=="sim":
    print(f"Boa sorte, {nome}!")
nota3=float(input("Digite sua terceira nota: "))
media2_total=float(media(media1_total,nota3))
print(media2_total)
if media2_total>=5:
      print(f"Parabéns, {nome}, você aproveitou a sua chance! Está aprovado.")
else:
      print(f"Sinto muito, {nome}, você não aproveitou sua chance. Estude mais para a próxima.")