import random


#1º armazenar funções, listas e matrizes
situação_objetos = ["Postado", "Não encontrado", "Entregue", "Não entregue"]

def registrar_encomenda():
     codigo = int(input("Insira o código do objeto: "))
     novo_registro = {"codigo": codigo, "status": "Postado"}
     


def conferencia_eletronica():
     
def remover_encomenda():


def gerar_codigo():
    codigo = [0, 0, 0, 0, 0]
    for i in range(len(codigo)):
        codigo[i] = random.randint(0, 9)



#2º criar parte do funcionário
def menu_funcionario():
    print('--- 🔧 MENU FUNCIONÁRIO 🔧 ---')
    print("1. Registrar nova encomenda")
    print("2. Conferência eletrônica (ver todas as encomendas)")
    print("3. Atualizar status ou remover encomenda")
    print("4. Voltar ao menu principal")
    entrada_usuario = ('Escolha uma opção: ')

    if entrada_usuario == 1:
         registrar_encomenda()
    elif entrada_usuario == 2:
         conferencia_eletronica()
    elif entrada_usuario == 3:
         remover_encomenda()
    elif entrada_usuario == 4:
         menu_principal()
         
#3º criar parte do cliente 

def menu_cliente():
    codigo = input("Digite o código de rastreamento do seu produto: ").strip
    for encomenda in encomendas:
        if encomenda["codigo"] == codigo:
            print(f"\nSeu objeto foi localizado!\nCódigo: {codigo} | Status: {encomenda['status']}\n")
            return
    print("O código fornecido não encontrado. Verifique e tente novamente.\n")

#4º menu
def menu_principal():
    print("\n--- 📦 Bem-vindo ao UniTrack! 📦 ---")
    print("Nosso sistema permite rastrear e gerenciar suas encomendas de forma fácil e rápida.")

    while True:
        print("\nVocê é:")
        print("1. Cliente")
        print("2. Funcionário")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
                menu_cliente()
        elif opcao == "2":
                menu_funcionario()
        elif opcao == "3":
            print("👋 Obrigado por usar o UniTrack. Volte sempre!\n")
            break
        else:
            print("❌ Opção inválida. Tente novamente.\n")