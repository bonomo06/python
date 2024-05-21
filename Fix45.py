def desconto1(x):
    return(x*0.80)
def desconto2(x):
    return(x*0.90)
def desconto3(x):
    return(x*0.95)
print("Pedro Henrique Bonomo Santos, 1051392411015, Desenvolvimento de Software Multiplataforma")
compra=float(input("Digite o valor da compra: "))
print(f"Valor da compra: {compra}")
if compra>=300.00:
    print(f"Valor da compra com desconto: {desconto1(compra)}")
elif compra>=200.00 and compra<=299.99:
    print(f"Valor da compra com desconto: {desconto2(compra)}")
elif compra<=199.99:
    print(f"Valor da compra com desconto: {desconto3(compra)}")