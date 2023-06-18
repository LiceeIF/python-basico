print("bem-vindo ao seu gerenciador de tarefas!")

#cria uma função para adicionar uma nova tarefa
def adicionar_tarefa(lista_tarefas):
    tarefa = input("Digite a nova tarefa: ")
# o método append aqui se é utilizado para armazenar um elemento numa lista 
# neste caso, uma tarefa está sendo inserida na lista de tarefas
    lista_tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")

#cria uma função para remover uma tarefa
def remover_tarefa(lista_tarefas):
    print("Lista de Tarefas:")
    exibir_tarefas(lista_tarefas)
#indice neste caso é uma variavel responsavel por armazenar o número da tarefa que o usuário deseja remover
    indice = int(input("Digite o número da tarefa a ser removida: "))
    if indice >= 0 and indice < len(lista_tarefas):
#pop() é um método em Python que remove e retorna um elemento de uma lista em uma determinada posição
        tarefa_removida = lista_tarefas.pop(indice)
        print(f"A tarefa '{tarefa_removida}' foi removida com sucesso!")
    else:
        print("Índice inválido. Por favor, digite um número de tarefa válido.")

def exibir_tarefas(lista_tarefas):
#len retorna o tamanho de uma lista, neste caso, verifica se a lista está vazia
    if len(lista_tarefas) == 0:
        print("A lista de tarefas está vazia.")
    else:
        print("Lista de Tarefas:")
# enumerate(lista_tarefas) é uma função que retorna um objeto enumerado contendo pares de índice-valor
        for i, tarefa in enumerate(lista_tarefas):
# aqui será exibido o número do índice seguido da tarefa na lista de tarefas
            print(f"{i}. {tarefa}")

#define uma função lista de tarefas:
def lista_de_tarefas():
    # cria uma nova lista vazia e a associa à variável lista_tarefas:
    lista_tarefas = []

#aqui será criado um loop infinito no programa até que ele seja interrompido
    while True:
        print("\nMenu:")
        print("1: Adicionar tarefa")
        print("2: Remover tarefa")
        print("3: Exibir tarefas")
        print("4: Sair")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == '1':
            adicionar_tarefa(lista_tarefas)
        elif opcao == '2':
            remover_tarefa(lista_tarefas)
        elif opcao == '3':
            exibir_tarefas(lista_tarefas)
        elif opcao == '4':
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

#aqui a função lista de tarefas está sendo chamada e enfim, será executada
lista_de_tarefas()