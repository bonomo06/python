maior_nota=None
for i in range(5):
    numero=float(input("Digite a nota e dê um enter: "))
    if maior_nota is None or numero>maior_nota:
        maior_nota=numero
print("A maior nota é: ", maior_nota)
print("Pedro Henrique Bonomo Santos, 1051392411015, Desenvolvimento de Software Multiplataforma")
while numero>10 or numero<0:
    print("Verifique se as notas estão digitadas de forma correta: ")
    for i in range(5):
        numero=input("Digite a nota e dê um enter: ")
    maior_nota=float
    if maior_nota is None or numero>maior_nota:
        maior_nota=numero
    print("A maior nota é: ", maior_nota)