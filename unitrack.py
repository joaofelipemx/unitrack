import csv

arquivo = "encomendas.csv" 
situação = ["Postado", "Em trânsito", "Entregue", "Não entregue"]

def carregar_encomendas():
    try:
        with open(arquivo, mode='r', newline='') as file:
            reader = csv.reader(file)
            return [linha for linha in reader][1:]
    except FileNotFoundError:
        return []

def salvar_encomendas(encomendas):
    with open(arquivo, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["codigo", "status"])  
        writer.writerows(encomendas)

def validar_codigo(codigo):
    return codigo.isdigit() and len(codigo) == 5

def registrar_encomenda(encomendas):
    codigo = input("Digite o código do produto (5 números): ").strip()
    
    if not validar_codigo(codigo):
        print("Código inválido! Deve conter exatamente 5 números.\n")
        return

    encomendas.append([codigo, "Postado"])
    salvar_encomendas(encomendas)
    print(f"\nEncomenda registrada com sucesso! Código: {codigo}\n")

def conferir_encomendas(encomendas):
    if not encomendas:
        print("\nNenhuma encomenda registrada.\n")
    else:
        print("\nLista de encomendas:")
        for encomenda in encomendas:
            print(f"Código: {encomenda[0]} | Status: {encomenda[1]}")
        print()

def atualizar_status(encomendas):
    codigo = input("Digite o código de rastreamento: ").strip()

    for i in range(len(encomendas)):
        if encomendas[i][0] == codigo:
            print(f"\nStatus atual: {encomendas[i][1]}")
            print("1 - Atualizar status")
            print("2 - Remover encomenda")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                novo_status = input(f"Novo status ({', '.join(situação)}): ").strip() 
                if novo_status in situação:
                    encomendas[i][1] = novo_status
                    salvar_encomendas(encomendas)
                    print("Status atualizado com sucesso!\n")
                else:
                    print("Status inválido.\n")
            elif opcao == "2":
                del encomendas[i]
                salvar_encomendas(encomendas)
                print("Encomenda removida com sucesso!\n")
            return
    
    print("Código não encontrado.\n")

def rastrear_encomenda(encomendas):
    codigo = input("Digite o código de rastreamento: ").strip()

    for encomenda in encomendas:
        if encomenda[0] == codigo:
            print(f"\nEncomenda encontrada!\nCódigo: {codigo} | Status: {encomenda[1]}\n")
            return
    
    print("Código não encontrado. Verifique e tente novamente.\n")

def exibir_menu_funcionario():
    print("\nMENU FUNCIONÁRIO")
    print("1. Registrar nova encomenda")
    print("2. Conferência eletrônica (ver todas as encomendas)")
    print("3. Atualizar status ou remover encomenda")
    print("4. Voltar ao menu principal")

def menu_funcionario(encomendas):
    while True:
        exibir_menu_funcionario()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            registrar_encomenda(encomendas)
        elif opcao == "2":
            conferir_encomendas(encomendas)
        elif opcao == "3":
            atualizar_status(encomendas)
        elif opcao == "4":
            break
        else:
            print("Opção inválida. Tente novamente.\n")

def exibir_menu_principal():
    print("\nBem-vindo ao UniTrack!")
    print("Nosso sistema permite rastrear e gerenciar suas encomendas de forma fácil e rápida.")
    print("\nVocê é:")
    print("1. Cliente")
    print("2. Funcionário")
    print("3. Sair")

def menu_principal():
    encomendas = carregar_encomendas()

    while True:
        exibir_menu_principal()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            rastrear_encomenda(encomendas)
        elif opcao == "2":
            menu_funcionario(encomendas)
        elif opcao == "3":
            print("Obrigado por usar o UniTrack. Até mais!\n")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

menu = menu_principal()
print(menu)