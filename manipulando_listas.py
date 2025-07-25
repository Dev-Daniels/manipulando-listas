print("-" * 53)
print("--- Bem vindo a Empresa do Daniel Lino de Almeida ---") # EXIGÊNCIA DE CÓDIGO 1 de 8
print("-" * 53)
print()

# EXIGÊNCIA DE CÓDIGO 2 de 8
lista_funcionario = [] # EXIGÊNCIA DE CÓDIGO 7 de 8
funcionario = {}
id_global = int(5118912)

# EXIGÊNCIA DE CÓDIGO 3 de 8
def cadastrar_funcionario(id):
    global id_global
    print("-"*45)
    print("-"*8,"MENU CADASTRAR FUNCIONÁRIO","-"*8)
    print("-"*45)
    print(f"Id funcionario: {id}")
    funcionario['id'] = int(id) # Armazena o valor inicial do id_global
    funcionario['nome'] = input("Nome do funcionário: ")
    funcionario['setor'] = input("Informe o setor: ")
    try: # Verificando que digite apenas ponto fluante EXIGÊNCIA DE CÓDIGO 8 de 8
        funcionario['salario'] = float(input("Informe o salário: R$ "))
    except ValueError: # Mesmo com erro, ele adicionava o funcionário sem salario
        print("Valor inválido, insira novamente!")
        return "" # então ele não salva caso ocorra erros
    else:
        # Apenas incrementa o id_global não der erro de valor
        lista_funcionario.append(funcionario.copy())
        id_global +=1
    return ""

# [EXIGÊNCIA DE CÓDIGO 4 de 8]
def consultar_funcionario():
    while True:
        print("-"*44)
        print("-"*8,"MENU CONSULTAR FUNCIONÁRIO","-"*8)
        print("-"*44)
        print("1 - Consultar Todos\n2 - Consultar por Id\n3 - Consultar por Setor\n4 - Retornar ao menu")
        consultar = input(">> ")
        print()
        match consultar:
            case "1":
                # verifica se tem cadastro(apenas caso for consultar todos sem cadastrar pelo menos uma pessoa)
                if not lista_funcionario:
                    print("Nenhum funcionário foi cadastrado.")
                # Consulta todos os funcionários cadastrados
                for funcionario in lista_funcionario:
                    for chave, valor in funcionario.items():
                        print(f"{chave}: {valor}")
                    print()

            case "2":
                id_func = False # Variavel para verificar se existe o ID
                try: # Como coloquei o id_global int, verifico que apenas numeros sejam digitados
                    info_id = int(input("Informe o ID: "))
                except ValueError:
                    print("Digite apenas números!")
                else:
                    for funcionario in lista_funcionario:   # Para cada funcionario em lista_funcionario,
                        if info_id == funcionario['id']:    # se for igual ao id,
                            for chave, valor in funcionario.items():    #então, print as chaves e valores de funcionario 
                                print(f"{chave} : {valor}")
                            id_func = True # Se o ID for igual o funcionario['id'], muda para True
                        # Variavel não foi verificada
                    if not id_func: # Se id_func não for 'executada' significa que o info_id não foi igual
                        print("ID não encontrado")
            case "3":
                setor = False # Para verficar setor
                # Mesma lógica para pegar o ID, apliquei no setor
                info_setor = input("Informe o setor: ")
                for funcionario in lista_funcionario:
                    if info_setor == funcionario['setor']:
                        for chave, valor in funcionario.items():
                            print(f"{chave} : {valor}")
                            setor = True # Caso IF seja verdadeiro
                        print() # Quebra de linha a cada funcionario
                if not setor: # Se não obtiver valor true dos IF, significa que o valor não é igual
                    print("Setor não encontrado!") # Caso If seja falso
            case "4": 
                return "" # Ele não retorna valor, e para o loop de consultar, voltando ao menu principal
            case _:
                print("Opção inválida")
                continue  

# [EXIGÊNCIA DE CÓDIGO 5 de 8]
def remover_funcionario():
    while True:
        print("-"*42)
        print("-"*8,"MENU REMOVER FUNCIONÁRIO","-"*8)
        print("-"*42)
        try:
            remover = int(input("Digite o ID do funcionário a ser removido: "))
        except ValueError: # Caso o valor não seja inteiro, printa na tela e refaz o loop
            print("Digite apenas números")
            continue
        else:
            func = False
            # Se remover for igual ao valor de id, então remove o funcionairo percorrido na lista
            for funcionario in lista_funcionario:   
                if remover == funcionario['id']:
                    lista_funcionario.remove(funcionario)
                    print("Funcionário removido com sucesso!") # Caso ocorra tudo certo, printa na tela
                    func = True
            if not func:
                print("ID inválido")
                continue
            break
    return"" # Para não retornar nada ao invés de 'none'

#Programa Principal | Main EXIGÊNCIA DE CÓDIGO 6 de 8
while True:
    print("-"*32)
    print("-"*8,"MENU PRINCIPAL","-"*8)
    print("Escolha a opção desejada:\n1 - Cadastrar Funcionários\n2 - Consultar Funcionário(s)\n3 - Remover Funcionário\n4 - Encerrar Programa")
    escolha = input(">> ")
    match escolha:
        case '1':
            print()
            print(cadastrar_funcionario(id_global))
            # Incrementando o ID toda vez que escolher o menu de cadastrar(escolha == '1')
        case '2':
            print() # Quebre de linha
            print(consultar_funcionario())

        case '3':
            print() # Quebre de linha
            print(remover_funcionario())

        case '4':
            print("Encerrado...")
            break

        case _: # Caso não seja entre 1 e 4
            print("Opção inválida, tente novamente!\n")
            continue