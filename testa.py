maior_nota = None
for i in range(5):
    numeros_str = input("Digite as notas separadas por espaço. (Ex: 6 7 8 9 10): ")
    numeros = [float(numero) for numero in numeros_str.split()]
    for numero in numeros:
        if maior_nota is None or numero > maior_nota:
            maior_nota = numero
print("A maior nota é:", maior_nota)