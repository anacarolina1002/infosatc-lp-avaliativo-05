nome=[]
sobrenome=[]
email=[]
senha=[]
celular=[]
endereco=[]
cpf=[]
import re

def menu():
    print('''
    1- Depositar
    2- Sacar
    3- Conferir Saldo
    4- Transferir
    5- Encerrar Conta
    ''')
    op = input("Digite a opção desejada: ") 
    return op 

def deposito():
    pass

def saque():
    pass

def confereSaldo():
    pass

def transfere():
    pass

def encerrarConta():
    pass

def nomeVal():
    print("Nome menor que o esperado!")
    novoNome=(input("Insira novamente seu nome:"))
    if (len(novoNome)>=3):
        nome.replace(nome,novoNome)   

def cadastroDados():
    nomeCont = 0
    sobrenomeCont = 0
    emailCont =0
    senhaCont=0
    numClientes=0
    while numClientes <5:
        nome=(input("Digite o seu nome:"))
        if (len(nome)<3):
            nomeVal()
        elif (len(nome)>=3):
            nomeCont+=1

        sobrenome=(input("Digite o seu sobrenome:"))
        while (len(sobrenome)<3):
            print("Sobrenome menor que o esperado!")
            novoSobrenome=str(input("Insira novamente seu sobrenome:"))
            if(len(novoSobrenome)>=3):
                sobrenome.replace(sobrenome,novoSobrenome)
        if (len(sobrenome)>=3 or (len(novoSobrenome)>=3)):
            sobrenomeCont+=1

        regex = re.compile('@') 
        email=(input("Digite o seu email:"))
        while(regex.search(email) == None):
            print("E-mail incorreto!")
            novoEmail=(input("Insira um novo e-mail:"))
            if(regex.search(novoEmail) != None):
                email.replace(email,novoEmail)
        if(regex.search(email) != None or (regex.search(novoEmail) != None)):
            emailCont+=1


        senha=(input("Digite sua senha:"))
        while (len(senha)<5):
            print("Senha menor que o esperado!")
            novaSenha=str(input("Insira novamente sua senha:"))
            senha.replace(senha,novaSenha)
        if (len(senha)>=5):
            senhaCont+=1

        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]') 
        while (regex.search(senha) == None):
            senhaNova=(input("Insira novamente sua senha:"))
            senha.replace(senha,senhaNova)
        if senha:
            senhaCont+=1

        cpf=(int(input("Digite seu cpf:")))
        endereco=(str(input("Digite seu endereço:")))
        celular=(str(input("Insira seu número de celular:")))

        numClientes = numClientes + 1

    if nomeCont==1 and sobrenomeCont==1 and emailCont==1 and senhaCont==1:
        print("Iniciando...")
        menu()

cadastroPessoa=input("Iniciar cadastro: 1-Sim ou 2-Não")
if cadastroPessoa=="1":
    print("Iniciando...")
    cadastroDados()
else:
    SystemExit

def lerOpcoes ():  
    pass  
    lerOpcoes() 
    opcao = menu() 
    while opcao != "9": 
        if opcao=="1": 
            deposito() 
        elif opcao=="2":
            saque()
        elif opcao=="3":
            confereSaldo()
        elif opcao=="4":
            transfere()
        elif opcao=="5":
            encerrarConta()

    opcao = menu() 





