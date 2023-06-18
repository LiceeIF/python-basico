#def está criando uma função para calculadora
def calculadora():
    print("Calculadora Simples")
    print("Selecione a operação:")
    print("1: soma")
    print("2: subtração")
    print("3: multiplicação")
    print("4: divisão")

#a variavel "opcao" verifica qual operação o usuario deseja efetuar 
    opcao = input("Insira o número da operação que você deseja fazer: ")

#este if com estes valores verifica se o valor da variável "opção" está presente na lista
    if opcao in ['1', '2', '3', '4']:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if opcao == '1':
            resultado = num1 + num2
            print("O resultado da adição é:", resultado)

#é comum utilizar uma sequência de if e elif em python pois o switch case não é uma estrutura de fluxo usada
        elif opcao == '2':
            resultado = num1 - num2
            print("O resultado da subtração é:", resultado)
        elif opcao == '3':
            resultado = num1 * num2
            print("O resultado da multiplicação é:", resultado)
        else:
            if num2 != 0:
                resultado = num1 / num2
                print("O resultado da divisão é:", resultado)
            else:
                print("Erro: Divisão por zero não é permitida.")
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

#Essa linha de código é responsável por iniciar a execução do programa da calculadora pois chama a função:
calculadora()