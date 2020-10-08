nomeLista=[]
sobrenomeLista=[]
senhaLista=[]
emailLista=[]
enderecoLista=[]
cpfLista=[]
celularLista=[]
saldoLista=[]
variavelLista=[]

def validaNome():
    nome=input("Insira seu primeiro e segundo nome(se tiver): ")
    print(nome)
    if len(nome)<3:
        op=("Nome menor que o esperado! Insira-o novamente: ")
        validaNome()       
    else:
            pass
    return nome

def validaSobrenome():
    sobrenome=input("Insira seu sobrenome: ")
    print(sobrenome)
    if len(sobrenome)<3:
        op=("Sobrenome menor que o esperado! Insira-o novamente: ")
        validaSobrenome()       
    else:
        pass
    return sobrenome

def validaSenha():
    senha=input("Insira uma senha: ")
    if(len(senha)<5):
        print("Senha menor que o esperado! Insira-a novamente: ")
        validaSenha()#volta para a função de pedir email
    else:
        return senha

    if "@"in senha:
        return senha 
    else:
        print("A senha precisa de pelo menos um caractere especial! Ex:@ ")
        print("Insira-a novamente!")
        validaSenha()

def validaEmail():
    email=input("Insira seu e-mail no formato user@email: ")
    if "@" in email:
        return email
    else:
        print("E-mail inválido! Digite-o novamente:")
        validaEmail()

def depositarBanco(variavel):
    deposito=float(input("Insira o valor a ser depositado: "))
    if deposito>0:
        print("Valor de",deposito,"R$ depositado com sucesso!")
        saldoLista[variavel]+=deposito

def saqueBanco(variavel):
    sacar=float(input("Insira a quantia de saque: "))
    if sacar <saldoLista[variavel]:
        print("O valor de",sacar,"R$ foi sacado com sucesso!")
        saldoLista[variavel]=(saldoLista[variavel])-(sacar)
    else:
        print('''Valor ultrapassou os limites de saldo! Digite: 
        1- Mudar valor
        2- Voltar ao menu de operações
        ''')#esse print com ''' eu vi num site e achei que ia ficar bom pro menu 
        #usei no outro menu tbm
        op=int(input("Digite o número da opção desejada:"))
        if op=="1":
            saqueBanco(variavel)
        else:
            menuOperacoes()

def verificaSaldo(variavel):
    print("Seu saldo equivale a:", saldoLista[variavel], "R$")
    #essa parte de saldo foi a que mais deu trabalho pq eu queria que ela fosse mudando
    #de acordo com as operações, daí vi essa forma de fazer em algum código e adaptei pro meu programa
    
def transfBanco(variavel):
    dinheiroTransf=float(input("Valor a ser enviado:"))
    if dinheiroTransf>0 and dinheiroTransf<saldoLista[variavel]:
        saldoLista[variavel] = saldoLista[variavel] - (dinheiroTransf)
    else:
        print('''Valor ultrapassou os limites de saldo! Digite: 
        1- Mudar valor
        2- Voltar ao menu de operações
        ''')
        op=int(input("Digite o número da opção desejada:"))
        if op=="1":
            transfBanco(variavel)
        else:
            menuOperacoes()

def cancelaBanco(variavel):
    print('''Você deseja mesmo finalizar esta operação? Digite:
    1-Finalizar
    2-Voltar ao menu de operações
     ''')
    op=int(input("Insira o número da opção desejada: "))
    if op=="1":
        print("Finalizando...")
        print("Operação finalizada!")
        raise SystemExit 
    else:
        menuOperacoes(variavel)
    return

def loginCliente():
    clienteEmail=input("Insira seu e-mail: ")
    clienteSenha=input("Insira sua senha: ")
    if clienteEmail in emailLista:
        #o index aqui vai retornar os valores referentes ao que tá no () de cada um
        if (clienteSenha in senhaLista) and (emailLista.index(clienteEmail)==senhaLista.index(clienteSenha)):
                menuOperacoes(emailLista.index(clienteEmail))
        else:
            print("Senha incorreta! Repita a operação:")
            loginCliente()
    else:
        print("E-mail incorreto! Repita a operação:")
        loginCliente()

def cadastroDados():
    nome=validaNome()
    sobrenome=validaSobrenome()
    senha=validaSenha()
    email=validaEmail()
    cpf=input("Insira seu CPF:")
    endereco=input("Insira seu endereço:")
    celular=input("Insira seu número de celular:")
    if nome!=False or sobrenome!=False or senha!=False or email!=False:
        nomeLista.append(nome)
        sobrenomeLista.append(sobrenome)
        senhaLista.append(senha)
        emailLista.append(email)
        enderecoLista.append(endereco)
        cpfLista.append(cpf)
        celularLista.append(celular)
        variavel=nomeLista.index(nome)
        saldoLista.append(0)

def menuOperacoes(variavel):
    while True:#''' de novo
        print('''
        1-Depósito
        2-Saque
        3-Verificação de saldo
        4-Transferência Bancária
        5- Finalizar operação''')
        op=int(input("Insira o número da operação escolhida: "))
        if op==1:
            depositarBanco(variavel)
        if op==2:
            saqueBanco(variavel)
        if op==3:
            verificaSaldo(variavel)
        if op==4:
            transfBanco(variavel)
        if op==5:
            cancelaBanco(variavel)
            
def menuOpcoes():
    while True:
        print('''
        1-Cadastro de cliente 
        2-Login de cliente 
        3-Sair ''')
        op = int(input("Insira o número da opção desejada: "))
        if(op==1):
            cadastroDados()
        if(op==2):
            loginCliente()
        if(op==3):
            raise SystemExit
    return
menuOpcoes()