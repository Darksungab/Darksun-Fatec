#Calculadora basica
import time
continuar_calculando = True

while continuar_calculando:    
    print(f"\nBem vindo(a) à Calculadora Básica")
    print("Digite dois valores inteiros:")
    while True:
        try:
            Valor_1 = int(input("Primeiro valor: "))
            break
        except ValueError:
            print("Valor inválido! Digite apenas números inteiros.")
    while True:        
        try:
            Valor_2 = int(input("Segundo valor: "))
            break
        except ValueError:
            print("Valor inválido! Digite apenas números inteiros.")

    print(f"Valores aceitos:")
    print(f"Primeiro valor: {Valor_1}")
    print(f"Segundo valor: {Valor_2}")

    print("Escolha a operação desejada:")
    print("(Digite o simbolo correspondente)")
    print("Adição (+)")
    print("Subtração (-)")
    print("Multiplicação (*)")
    print("Divisão (/)")

    def verifica_operacao(opcao, Valor_1, Valor_2):
        if opcao == '+':
            resultado = Valor_1 + Valor_2
            operacao = "adição"
            print("Processando sua operação", end="")
            for i in range(3):
                print(".", end="", flush=True)
                time.sleep(0.6)
            print(f"\nResultado da {operacao}: {resultado}") 
        elif opcao == '-':
            resultado = Valor_1 - Valor_2
            operacao = "subtração"
            print("Processando sua operação", end="")
            for i in range(3):
                print(".", end="", flush=True)
                time.sleep(0.6)
            print(f"\nResultado da {operacao}: {resultado}")
        elif opcao == '*':
            resultado = Valor_1 * Valor_2
            operacao = "multiplicação"
            print("Processando sua operação", end="")
            for i in range(3):
                print(".", end="", flush=True)
                time.sleep(0.6)
            print(f"\nResultado da {operacao}: {resultado}")
        elif opcao == '/':
            if Valor_2 != 0:
                resultado = Valor_1 / Valor_2
                operacao = "divisão"
                print("Processando sua operação", end="")
                for i in range(3):
                    print(".", end="", flush=True)
                    time.sleep(0.6)
                print(f"\nResultado da {operacao}: {resultado}")
            else:
                print("Processando sua operação", end="")
                for i in range(3):
                    print(".", end="", flush=True)
                    time.sleep(0.6)
                print(f"\nErro: Divisão por zero não é permitida.")
    while True:
        opcao = input("Digite a opção desejada: ")   
        if opcao in ['+', '-', '*', '/']:
            verifica_operacao(opcao, Valor_1, Valor_2)
            break
        else:
            print("Opção inválida! Digite um dos símbolos: +, -, *, /")
    while True:
        resposta = input("\nDeseja fazer outro cálculo? (s/n): ").lower().strip()
        if resposta in ['s', 'sim']:
            print("Abrindo novo cálculo", end="")
            for i in range(3):
                print(".", end="", flush=True)
                time.sleep(0.6)
            break
        elif resposta in ['n', 'não', 'nao']:
            continuar_calculando = False
            break
        else:
            print("Digite 's' para SIM ou 'n' para NÃO")
time.sleep(1)
print("\nObrigado por usar a Calculadora!")
time.sleep(1)
print("Desenvolvido por Gabriel F. Ribeiro")
time.sleep(1)
print("Calculadora Encerrada.")