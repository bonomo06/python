import sys
def media(x,y):
    return (x*4 + y*6)/ 10
def add_ra(ra):
    nomearquivo= 'ra.txt'
    with open(nomearquivo, 'w') as file:
          file.write(ra + '\n')
arquivo='ra.txt'
def add_senha(senha):
     nome2arquivo='senha.txt'
     with open(nome2arquivo, 'w') as file:
          file.write(senha + '\n')
arquivo2='senha.txt'
print("Vamos fazer seu cadastro")
professor=str(input("Você é professor ou aluno? (Digite p ou a) "))
while professor.lower()=="a":
      print("A plataforma é só para professores.")
      sys.exit()
ra=input("Digite seu RA: ")
senha=input("Crie uma senha: ")
print("Muito bem! Cadastrado.")
add_ra(ra)
add_senha(senha)
confirmra=input("Digite o ra cadastrado: ")
confirmsenha=input("Digite a senha cadastrada: ")
with open('ra.txt', 'r') as file:
     conteudora=file.read()
with open('senha.txt', 'r') as file:
     conteudosenha=file.read()
if confirmra in conteudora and confirmsenha in conteudosenha:
     print("Muito bem! Você entrou")
elif confirmra not in conteudora and confirmsenha not in conteudosenha:
     print("Você errou")
'''se eu quiser adicionar sem reescrever o ra.txt ou o senha.txt, devo trocar o w por a'''