def imcf (x,y):
    return x/y**2
def imcm (x,y):
    return x/y**2
h=float(input("Digite sua altura(em metros): "))
kg=float(input("Digite seu peso em quilos(ex: 70.5): "))
sexo=str(input("Você é homem ou mulher? (Escreva h ou m) "))
print("Pedro Henrique Bonomo Santos, 1051392411015, Desenvolvimento de Software Multiplataforma")
if sexo.lower()=="m":
    if imcf(kg,h) < 19:
        print("Abaixo do peso")
        print(f"Este é seu IMC: {imcf(kg,h)}")
    elif imcf(kg,h) >= 19 and imcf(kg,h) < 24:
        print("Peso ideal")
        print(f"Este é seu IMC: {imcf(kg,h)}")
    elif imcf(kg,h) >= 24:
        print("Acima do peso")
        print(f"Este é seu IMC: {imcf(kg,h)}")
if sexo.lower()=="h":
    if imcm(kg,h) < 20:
        print("Abaixo do peso")
        print(f"Este é seu IMC: {imcm(kg,h)}")
    elif imcm(kg,h) >= 20 and imcm(kg,h) < 25:
        print("Peso ideal")
        print(f"Este é seu IMC: {imcm(kg,h)}")
    elif imcm(kg,h) >= 25:
        print("Acima do peso")
        print(f"Este é seu IMC: {imcm(kg,h)}")