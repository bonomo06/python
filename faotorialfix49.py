def calcular_fatorial(numero):
    if numero < 0:
        return "Número inválido. Escolha um número positivo, por favor"
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    return f"O fatorial de {numero} é {fatorial}."
numero = int(input("Digite um número inteiro positivo: "))
print("Pedro Henrique Bonomo Santos, 1051392411015, Desenvolvimento de Software Multiplataforma")
print(calcular_fatorial(numero))