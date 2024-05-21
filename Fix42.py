def media(x,y):
    return(x+y)/2
nome=input(str("Nome: "))
ra=input(str("RA: "))
nota1=float(input("Digite a nota da sua primeira prova: "))
nota2=float(input("Digite a nota da sua segunda prova: "))
print("Pedro Henrique Bonomo Santos, 1051392411015, Desenvolvimento de Software Multiplataforma")
resultado_media=media(nota1,nota2)
print(resultado_media)
if resultado_media>=7:
    print("Parabéns, você está aprovado!")
else:
    print("Você  ainda  tem  uma  chance!  Estude  mais  para  o exame.")