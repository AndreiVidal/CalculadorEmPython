def menuCalc():
    print(('=' * 15),'Python Calculator', ('=' * 15) )
    print("""
    Qual operação deseja realizar:
    [1] - Adiçao:
    [2] - Subtração:
    [3] - Multiplicação:
    [4] - Divisão:
    [5] - Sair
    
    """)


while True:
    menuCalc()
    opcao = input('Digite a opção desejada: ')
    if not opcao.isnumeric() or opcao >= '6':
        print('Opção inválida!!')
        print('Digite uma das seguintes opções (1/2/3/4/5)')
        continue
    else:
        opcao = int(opcao)
    if opcao == 5:
        break
    num1 = input('Digite um Número: ')
    num2 = input('Digite outro número: ')
    if not num1.isnumeric() or not num2.isnumeric():
        print('Digite apenas números')
    else:
        num1 = int(num1)
        num2 = int(num2)

    if opcao == 1:
        print(f'O resultado da adição é: {num1+num2}')
    elif opcao == 2:
        print(f'O resultado da subtração é: {num1 - num2}')
    elif opcao == 3:
        print(f'O resultado da multiplicação é: {num1 * num2}')
    elif opcao == 4:
        div = num1 / num2
        print(f'O resultado da divisão é: {div:.2f}')

    else:
        print('Digite uma opção válida!')
