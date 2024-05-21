nota1=float(input("Insira a primeira nota: "))
nota2=float(input("Insira a segunda nota: "))
nota3=float(input("Insira a terceira nota: "))
while nota1 < 0 or nota2 < 0 or nota3 < 0 or nota1 > 10 or nota2 > 10 or nota3 > 10:
    print("As notas devem ser maiores ou iguais a 0")
    nota1=float(input("Insira a primeira nota: "))
    nota2=float(input("Insira a segunda nota: "))
    nota3=float(input("Insira a terceira nota: "))
    nota4=(nota1+nota2+nota3)/3
print(f"Média final: {nota4}")
if nota4>=6:
    print("Aprovado")
else:
    print("Reprovado")