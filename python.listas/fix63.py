def add_msg():
    nomearquivo='mensagem.txt'
    mensagens=[]
    for i in range(4):
        mensagem=input("Digite uma mensagem: ")
        mensagens.append(mensagem + '\n')
    with open(nomearquivo, 'w') as file:
          file.writelines(mensagens)
    with open(nomearquivo, 'r') as file:
         conteudo=file.read()
    tamanho=len(conteudo)
    print(f"Tamanho da variável mensagem.txt é {tamanho}")
arquivo='mensagem.txt'
add_msg()
with open('mensagem.txt', 'r') as file:
    conteudo=file.read()
print(f"Isso foi salvo: {conteudo}")
print("Pedro Henrique Bonomo Santos RA:1051392411015 Desenvolvimento de Software Multiplataforma")