def add_senha():
    arquivo_nome= 'senha.txt'
    senhas=[]
    for i in range(5):
        senha=input("Digite as senhas, por favor: ")
        senhas.append(senha + '\n')
    with open(arquivo_nome, 'w') as file:
        file.writelines(senhas)
    print("Senhas adicionadas com sucesso")
arquivo= 'senha.txt'
print("Pedro Henrique Bonomo Santos RA:1051392411015 Desenvolvimento de Software Multiplataforma")
add_senha()