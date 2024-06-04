def calcula_media(x,y):
    return (x*4 + y*6) / 10
nome=str(input("Nome do aluno: "))
NP1=float(input("Nota da 1° prova: "))
NP2=float(input("Nota da 2° prova: "))
print("Pedro Henrique Bonomo Santos RA:1051392411015 Desenvolvimento de Software Multiplataforma")
print("Essa é sua média: ", calcula_media(NP1,NP2))
if calcula_media(NP1,NP2)>=7:
    print(f"Parabéns, {nome}, você está aprovado!")
elif calcula_media(NP1,NP2)<=6.99:
    print(f"Sinto muito, {nome}, você precisa fazer outro exame.")
elif calcula_media(NP1,NP2)<=2.99:
    print(f"Sinto muito, {nome}, você está de DP.")