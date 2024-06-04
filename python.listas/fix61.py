def add_emails():
    arquivo_nome= 'email.txt'
    emails=[]
    for i in range (3):
        email=str(input("Digite os emails, por favor: "))
        emails.append(email + "\n")
    with open(arquivo_nome, 'w') as file: #aqui para adicionar os emails
        file.writelines(emails)
    print("E-mails adicionados com sucesso!")
arquivo = 'email.txt' # Nome do arquivo
print("Pedro Henrique Bonomo Santos RA:1051392411015 Desenvolvimento de Software Multiplataforma")
add_emails()