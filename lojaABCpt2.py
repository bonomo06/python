compra=float(input("Valor da compra: "))
desconto1=compra*0.80
desconto2=compra*0.90
desconto3=compra*0.95
print(f"Valor da compra sem desconto: {compra}")
print("Pedro Henrique Bonomo Santos, 1051392411015, Desenvolvimento de Software Multiplataforma")
if compra<199.99:
    print(f"Valor da compra com desconto: {desconto3}")
elif compra>=200.00 and compra<299.99:
    print("Seu desconto foi de 10%")
    print(f"Valor da compra com desconto: {desconto2}")
elif compra>=300.00:
    print("Seu desconto foi de 20%")
    print(f"Valor da compra com desconto: {desconto1}")