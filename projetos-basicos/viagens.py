def adicionar_viagem(lista_viagens):
    destino = input("Digite um novo destino que você deseja visitar: ")
    lista_viagens.append(destino)
    print("Destino adicionado à lista com sucesso!")

def remover_destino():
    destino = input("Digite o nome do lugar a ser removido: ")
    if destino in lista_viagens:
        lista_viagens.remove(destino)
        print(f"{destino} foi removido da lista de lugares para visitar.")
    else:
        print(f"{destino} não está na lista de destinos para visitar.")

def mostrar_destino():
    print("lugares do mundo para visitar:")
    if lista_viagens:
        for destino in lista_viagens:
            print("- " + destino)
    else:
        print("A lista de destinos está vazia.")

def sair():
    print("O programa foi encerrado.")
    exit()

lista_viagens = []

while True:
    print("\nMenu:")
    print("1:. Adicionar lugar")
    print("2: Remover lugar")
    print("3: Mostrar lugares")
    print("4: Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        adicionar_viagem(lista_viagens)
    elif opcao == "2":
        remover_destino(lista_viagens)
    elif opcao == "3":
        mostrar_destino()
    elif opcao == "4":
        sair()
    else:
        print("Opção inválida. Digite uma opção válida.")