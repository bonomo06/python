import sys
def media(x,y):
    return (x*4 + y*6)/ 10
print("Vamos fazer seu cadastro")
professor=str(input("Você é professor ou aluno? (Digite p ou a) "))
while professor.lower()=="a":
      print("A plataforma é só para professores.")
      sys.exit()
ra=int(input("Digite seu RA: "))
senha=int(input("Crie uma senha só com números: "))
print("Muito bem! Cadastrado.")
if professor.lower()=="p":
    print("Olá professor.")
    confirmra=int(input("Digite o RA cadastrado: "))
    confirmsenha=int(input("Digite a senha criada: "))
    while confirmra!=ra or confirmsenha!=senha:
          print("Tente novamente")
          confirmra=int(input("Digite o RA cadastrado: "))
          confirmsenha=int(input("Digite a senha criada: "))
    if confirmra==ra and confirmsenha==senha:
        nota1=float(input("Digite a primeira nota: "))
        nota2=float(input("Digite a segunda nota: "))
        print(media(nota1,nota2))
        if media(nota1,nota2)>=7.0:
                print("APROVADO")
        elif media(nota1,nota2)<7 and media(nota1,nota2)>3:
                print("EXAME")
        elif media(nota1,nota2)<3:
                print("DP")
print("Pedro Henrique Bonomo Santos, 1051392411015, Desenvolvimento de Software Multiplataforma")