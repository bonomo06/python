def media(x,y):
    return (x*4 + y*6)/ 10
nota1=float(input("Digite sua primeira nota: "))
nota2=float(input("Digite sua segunda nota: "))
print(media(nota1,nota2))
print("Pedro Henrique Bonomo Santos, 1051392411015, Desenvolvimento de Software Multiplataforma")
if media(nota1,nota2)>=7.0:
    print("APROVADO")
elif media(nota1,nota2)<7 and media(nota1,nota2)>3:
    print("EXAME")
elif media(nota1,nota2)<3:
    print("DP")