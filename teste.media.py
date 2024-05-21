nota1=float (input("Nota 1° prova: "))
nota2=float (input("Nota 2° prova: "))
nota3=float (input("Nota 3° prova: "))
nota4=(nota1+nota2+nota3)/3
print(f"Média final: {nota4}") #o f junto com colchetes serve para escrever e colocar uma varaivel também, fazendo isso, o terminal vai mostrar o escrito e a variavel
if nota4>=6: #o maior vem antes
    print("Aprovado")
else:
    print("Reprovado")