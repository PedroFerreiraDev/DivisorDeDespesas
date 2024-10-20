usuarios = []
saldo = 0
cofres = []

def cadastro():

    global usuarios
    finalizador = "n"

    while finalizador == "n":

        usuario = {}
    
        usuario['login'] = input("Login: ")
        usuario['senha'] = input("Senha: ")

        usuarios.append(usuario)
    
        finalizador = input("Para finalizar o cadastro digite (s).")

def login():
    global usuarios
    
    login_input = input("Usuário: ")
    senha_input = input("Senha: ")
    
    for usuario in usuarios:
        if usuario['login'] == login_input and usuario['senha'] == senha_input:
            return True  
    return False  

def excluir():

    global usuarios
    procurador = input("Digite o login do usuário que deseja excluir: ")
    confirm = input("Digite a senha do usuário que deseja excluir: ")

    for usuario in usuarios:
        if usuario['login'] == procurador and confirm == usuario['senha']:
            usuarios.remove(usuario)
            print("Usuário removido com sucesso! ")

def InOut():
    
    global saldo
    
    option = input(" (1)Add Saldo\n (2)Remover Saldo")
    if option == "1":
        adicionar = float(input("Adicionar Saldo: "))
        saldo = saldo + adicionar
    elif option == "2":
        remover = float(input("Remover Saldo:"))
        saldo = saldo - remover
    else:
        print("Selecione uma opção válida! ")

def addclasses():
    
    global cofres 
    continuar = "s"
    
    while continuar == "s":
        nome_cofre = input("Nome do cofre: ")
        valor_cofre = 0
        cofrinhos = {
            "nome" : nome_cofre, 
            "saldo": valor_cofre
        }
        cofres.append(cofrinhos)
        
        continuar = input("Deseja adicionar mais um cofre? (s/n)").lower()

def addvalorclasse():
    
    global saldo
    global cofres
    
    findcofre = input("Qual cofre deseja adicionar o valor: ")
    addvalor = float(input("Adicionar valor ao cofre: "))
    
    if addvalor <= saldo:
        for cofrinho in cofres:
            if cofrinho["nome"] == findcofre:
                cofrinho["saldo"] += addvalor
                saldo -= addvalor
            else: 
                print("Cofre não encontrado! ")
    else:
        print("Saldo Insuficiente! ")

def ver_cofres():
    global cofres
    if len(cofres) > 0:
        print("|  Cofres Disponíveis:\n|")
        for cofrinho in cofres:
            print(f"|  Cofre: {cofrinho['nome']} - Saldo: {cofrinho['saldo']}")
    else:
        print("|  Nenhum cofre disponível.")

def removervalorclasse():
    
    global saldo
    global cofres
    
    findcofre = input("Qual cofre deseja remover o valor: ")
    removervalor = float(input("Remover valor do cofre: "))
    

    for cofrinho in cofres:
        if cofrinho["nome"] == findcofre:
            if removervalor <= cofrinho["saldo"]:
                cofrinho["saldo"] -= removervalor
                saldo += removervalor    
            else:
                print("Saldo Insuficiente! " )
        else:
            print("Cofre não encontrado! ")

def excluirclasse():

    global saldo
    global cofres

    removerclass = input("Qual cofre deseja remover: ")
    
    for cofrinho in cofres:
        if cofrinho["nome"] == removerclass:
            saldo += cofrinho["saldo"]
            cofres.remove(cofrinho)  
            print("Cofre removido! ")
            return
        
def menu_principal():
    print("|  BEM VINDO AO SEU APLICATIVO DE CONTROLE DE GASTOS\n|\n|  Selecione a opção desejada:\n|")
    menu = input("|  (1)Cadastro\n|  (2)Login\n|  (3)Excluir Usuário\n")

    if menu == "1":
        cadastro()
        menu_principal()
    elif menu == "2":
        if login():
            print("|  Login efetuado com sucesso!\n|")
            menu_usuario()
        else:
            print("Usuário ou Senha incorretos!")
            menu_principal()
    elif menu == "3":
        excluir()
        menu_principal()
    else:
        print("Selecione uma opção válida")
        menu_principal()

def menu_usuario():
    print(f"|  Menu do Usuário [Saldo:{saldo}]\n|\n|  Selecione a opção desejada:\n|")
    option = input("|  (1)Adicionar Cofre\n|  (2)Adicionar/Remover Saldo\n|  (3)Adicionar Valor ao Cofre\n|  (4)Remover Valor do Cofre\n|  (5)Excluir Cofre\n|  (6)Ver Cofres e Valores\n|  (7)Sair\n")

    if option == "1":
        addclasses()
        menu_usuario()
    elif option == "2":
        InOut()
        menu_usuario()
    elif option == "3":
        addvalorclasse()
        menu_usuario()
    elif option == "4":
        removervalorclasse()
        menu_usuario()
    elif option == "5":
        excluirclasse()
        menu_usuario()
    elif option == "6":
        ver_cofres()  
        menu_usuario()
    elif option == "7":
        print("Você saiu do sistema.")
    else:
        print("Selecione uma opção válida")
        menu_usuario()


menu_principal()