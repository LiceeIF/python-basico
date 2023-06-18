def adicionar_saldo():
    descricao = input("Digite a descrição da entrada de valor: ")
    valor = float(input("Digite o valor que você recebeu, insira um '.' caso tenha casas decimais: "))
    income = (descricao, valor)
    lista_income.append(income)
    print("O seu saldo foi atualizado com sucesso!")

def pagar_cartao():
    valor = float(input("Digite o valor do pagamento do cartão, insira um '.' caso tenha casas decimais: "))
    lista_income.append(("Pagamento do cartão", -valor))
    print("Pagamento do cartão registrado.")

def pagar_conta():
    descricao = input("Digite a descrição da conta: ")
    valor = float(input("Digite o valor da conta, insira um '.' caso tenha casas decimais: "))
    lista_income.append((f"Pagamento de conta: {descricao}", -valor))
    print("Pagamento de conta registrado.")
def mostrar_financas():
    saldo = calcular_saldo()
    print("as finanças de maneira organizada:")
    print("----------")
    for income in lista_income:
        print(f"{income[0]}: R${income[1]:.2f}")
    print("----------")
    print(f"Saldo atual: R${saldo:.2f}")

def calcular_saldo():
    saldo = 0
    for income in lista_income:
        saldo += income[1]
    return saldo

def sair():
    print("O programa foi encerrado.")
    exit()

lista_income = []

while True:
    print("\nMenu:")
    print("1: Adicionar despesa")
    print("2: Pagar cartão")
    print("3: Pagar conta")
    print("4: Mostrar finanças")
    print("5: Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        adicionar_saldo()
    elif opcao == "2":
        pagar_cartao()
    elif opcao == "3":
        pagar_conta()
    elif opcao == "4":
        mostrar_financas()
    elif opcao == "5":
        sair()
    else:
        print("Essa ação não pode ser efetuada. Escolha uma opção válida!")
