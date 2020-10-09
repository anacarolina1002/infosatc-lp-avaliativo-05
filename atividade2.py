nomeLista=[]
sobrenomeLista=[]
senhaLista=[]
emailLista=[]
enderecoLista=[]
cpfLista=[]
celularLista=[]
saldoLista=[]
variavelLista=[]
listaGeral=[]

def validaNome():#def onde o nome vai ser perguntado e depois uma linha de comandos vai ser executada
    nome=input("Insira seu primeiro e segundo nome(se tiver): ")#pergunta e inserção do nome
    print(nome)#nome aparece no monitor
    if len(nome)<3:#se o número de letras do nome inserido for menor que 3 executa o if
        print("Nome menor que o esperado! Insira-o novamente abaixo:")
        validaNome()#pede o nome novamente     
    else:
            pass#se o nome for >= ele passa pra próxima pergunta
    return nome

def validaSobrenome():
    sobrenome=input("Insira seu sobrenome: ")#pergunta e inserção do sobrenome
    print(sobrenome)#o sobrenome aparece no terminal
    if len(sobrenome)<3:#se ele for menor que 3 executa os comandos dentro do if
        print("Sobrenome menor que o esperado! Insira-o novamente abaixo:")
        validaSobrenome()# pede o sobrenome de novo     
    else:
        pass#senão for <3 ele executa normalmente e passa pro próximo
    return sobrenome

def validaSenha():
    senha=input("Insira uma senha: ")
    if(len(senha)<5):#se a senha for menor que 5, uma msg de erro aparece
        print("Senha menor que o esperado! Insira-a novamente: ")
        validaSenha()#volta para a função de pedir senha
    else:
        return senha

    if "@"in senha:#um caracter especial é necessário na senha, aqui é uma verificação se esse caracter ta presente
        return senha 
    else:#se não estiver...
        print("A senha precisa de pelo menos um caractere especial! Ex:@ ")
        print("Insira-a novamente!")
        validaSenha()#pede de novo

def validaEmail():
    email=input("Insira seu e-mail no formato user@email: ")
    if "@" in email: 
        return email
    else:#praticamente o mesmo esquema da senha, se não tiver o "@" ele dá erro e pede de novo
        print("E-mail inválido! Digite-o novamente:")
        validaEmail()

def depositarBanco(variavel):#aqui começa a parte de chatice mediana
    deposito=float(input("Insira o valor a ser depositado: "))
    if deposito>0:#se o depósito for maior que 100 ele deposita certinho(valor positivo)
        print("Valor de",deposito,"R$ depositado com sucesso!")
        saldoLista[variavel]+=deposito#o saldo da minha conta vai mudando conforme eu deposito

def saqueBanco(variavel):
    sacar=float(input("Insira a quantia de saque: "))
    if sacar <saldoLista[variavel]:#se o valor de saque for menor do que o que eu tenho no saldo ele vai de boa
        print("O valor de",sacar,"R$ foi sacado com sucesso!")
        saldoLista[variavel]=(saldoLista[variavel])-(sacar)#meu saldo muda conforme eu saco
    else:
        print('''Valor ultrapassou os limites de saldo! Digite: 
        1- Mudar valor
        2- Voltar ao menu de operações
        ''')#esse print com ''' eu vi num site e achei que ia ficar bom pro menu 
        #usei no outro menu tbm
        op=int(input("Digite o número da opção desejada:"))
        if op=="1":
            saqueBanco(variavel)#pede o valor de saque de novo
        else:
            menuOperacoes()# ou volta pro menu de operações pra fazr outra coisa

def verificaSaldo(variavel):
    print("Seu saldo equivale a:", saldoLista[variavel], "R$")
    #essa parte de saldo foi a que mais deu trabalho pq eu queria que ela fosse mudando
    #de acordo com as operações, daí vi essa forma de fazer em algum código e adaptei pro meu programa
    
def transfBanco(variavel):
    dinheiroTransf=float(input("Valor a ser enviado:"))
    if dinheiroTransf>0 and dinheiroTransf<saldoLista[variavel]:
        saldoLista[variavel] += saldoLista[variavel] - (dinheiroTransf)
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


def consultaCliente(variavel):#aqui busca o cliente pela posição dele [variavel] e imprime os dados
    print("Buscando...")
    print("Pessoa encontrada!")
    print("Nome: ",nomeLista[variavel])
    print("Sobrenome: ",sobrenomeLista[variavel])
    print("Senha: ",senhaLista[variavel])
    print("E-mail: ",emailLista[variavel])
    print("Endereço: ",enderecoLista[variavel])
    print("CPF: ",cpfLista[variavel])
    print("Celular: ",celularLista[variavel])
    print("Saldo da conta:",saldoLista[variavel])

def consultaLista(): #aqui mostra todas as pessoas com os dados delas
    tamanhoLista=(len(nomeLista))
    for variavel in range(tamanhoLista):
        print("Nome: ",nomeLista[variavel])
        print("Sobrenome: ",sobrenomeLista[variavel])
        print("Senha: ",senhaLista[variavel])
        print("E-mail: ",emailLista[variavel])
        print("Endereco: ",enderecoLista[variavel])
        print("CPF: ",cpfLista[variavel])
        print("Celular: ",celularLista[variavel])
        print("Saldo da conta: ",saldoLista[variavel])

def delCliente(variavel): #aqui apaga tudo de um determinado cliente, eu tentei usar uma lista só mas n deu muito certo 
    del nomeLista[variavel]
    del sobrenomeLista[variavel]
    del senhaLista[variavel]
    del emailLista[variavel]
    del enderecoLista[variavel]
    del cpfLista[variavel]
    del celularLista[variavel]
    del saldoLista[variavel]
    print("Lista com cliente removido: ")
    consultaLista()

def atualizaCliente(variavel):#aqui muda o valor de alguma opção que o cliente quiser mudar
    print('''Informações disponíveis para alteração:
    1-Nome
    2-Sobrenome
    3-CPF
    4-Email
    5-Endereço
    6-Celular
    7-Senha
    ''')
    menuAtualização(variavel)#aqui ele vai pro menu com as opções de mudança

def menuAtualização(variavel):
    op=int(input("Insira a opção que será atualizada: "))
    if op==1:
        nomeLista[variavel]=validaNome()#cada um pede o valor alterado e imprime a lista com o valor alterado
        print("Lista com valor alterado:")
        consultaLista()
    elif op==2:
        sobrenomeLista[variavel]=validaSobrenome()
        print("Lista com valor alterado:")
        consultaLista()
    elif op==3:
        cpfLista[variavel]=input("Insira seu CPF:")
        print("Lista com valor alterado:")
        consultaLista()
    elif op==4:
        emailLista[variavel]=input("Insira seu E-mail: ")
        print("Lista com valor alterado:")
        consultaLista()
    elif op==5:
        enderecoLista[variavel]=input("Insira seu endereço: ")
        print("Lista com valor alterado:")
        consultaLista()
    elif op==6:
        celularLista[variavel]=input("Insira seu número de celular: ")
        print("Lista com valor alterado:")
        consultaLista()
    elif op==7:
        senhaLista[variavel]=validaSenha()
        print("Lista com valor alterado:")
        consultaLista()

def operacoesAdm(variavel):
    print('''
1- Consultar um cliente
2- Consultar lista de clientes
3- Deletar um cliente
4- Atualizar dados de um cliente específico.
5- Sair do menu de administrador   
    ''')
    menuAdm(variavel) 

def loginUsuario(variavel):
    nomeUsuario=input("Insira seu nome de usuário: ")
    senhaUsuario=input("Insira a senha do usuário:")
    print("Usuário: ",nomeUsuario,"Senha: ",senhaUsuario)
    print("Carregando menu de administrador...")
    print("Olá usuário",nomeUsuario,"! Escolha uma das opções abaixo:")
    operacoesAdm(variavel)

def cadastroDados():
    nome=validaNome()#somente esses são () pq eles tem validações pra funcionar
    sobrenome=validaSobrenome()
    senha=validaSenha()
    email=validaEmail()
    cpf=input("Insira seu CPF:")
    endereco=input("Insira seu endereço:")
    celular=input("Insira seu número de celular:")
    if nome!=False or sobrenome!=False or senha!=False or email!=False:#se todas as informações retornaram em true
        nomeLista.append(nome)#esse append funciona como um englobamento, nomeLista engloba a variavel nome
        sobrenomeLista.append(sobrenome)
        senhaLista.append(senha)
        emailLista.append(email)
        enderecoLista.append(endereco)
        cpfLista.append(cpf)
        celularLista.append(celular)
        variavel=nomeLista.index(nome)
        saldoLista.append(0)
        print(f'''
Nome completo: {nome} {sobrenome} 
Senha: {senha} 
E-mail: {email} 
Endereço: {endereco} 
CPF: {cpf} 
Celular: {celular}''')

def menuAdm(variavel):#menu de opções do administrador
    op=(int(input("Insira a opção escolhida: ")))
    if op==1:
        print("Carregando...")
        variavel=int(input("Insira o número de posição da pessoa a ser buscada: "))
        consultaCliente(variavel)
    if op==2:
        print("Carregando...")
        consultaLista()
    if op==3:
        print("Carregando...")
        variavel=int(input("Insira o número de posição da pessoa a ser deletada: "))
        delCliente(variavel)
    if op==4:
        print("Carregando...")
        variavel=int(input("Insira o número da posição da pessoa a ser alterada: "))
        atualizaCliente(variavel)


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
            
def menuOpcoes(variavel):
    while True:
        print('''
        1-Cadastro de cliente 
        2-Administração
        3-Sair ''')
        op = int(input("Insira o número da opção desejada: "))
        if(op==1):
            cadastroDados()
        if(op==2):
            loginUsuario(variavel)
        if(op==3):
            raise SystemExit
    return
variavel=[]
menuOpcoes(variavel)#programa começa