from funcoes import soma
from funcoes import multiplicacao
from funcoes import divisao
from funcoes import subtracao
from funcoes import raiz
from funcoes import elevacao

while True:
    escolha = int(input('Digite 1 para fazer uma soma. \n'
                        'Digite 2 para fazer uma multiplição. \n'
                        'Digite 3 para fazer uma divisão. \n'
                        'Digite 4 para fazer uma subtração. \n'
                        'Digite 5 para fazer uma raiz quadrada. \n'
                        'Digite 6 para fazer uma calculo de elevação exemplo ao quadrado ao cubo ... \n'
                        'Faça sua escolha: '))

    if escolha == 1:
        valor1 = int(input('Digite o primeiro valor: '))
        valor2 = int(input('Digite o segundo valor: '))

        resultado = soma(valor1, valor2)
        print('-----------------------------------')
        print(f'O resultado da soma é: {resultado}')
        print('-----------------------------------')
        continue


    if escolha == 2:
        valor1 = int(input('Digite o primeiro valor: '))
        valor2 = int(input('Digite o segundo valor: '))

        resultado = multiplicacao(valor1, valor2)
        print('--------------------------------------------')
        print(f'O resultado da multiplicação é: {resultado}')
        print('--------------------------------------------')
        continue


    if escolha == 3:
        valor1 = int(input('Digite o primeiro valor: '))
        valor2 = int(input('Digite o segundo valor: '))

        resultado = divisao(valor1, valor2)
        print('--------------------------------------')
        print(f'O resultado da divisão é: {resultado}')
        print('--------------------------------------')
        continue


    if escolha == 4:
        valor1 = int(input('Digite o primeiro valor: '))
        valor2 = int(input('Digite o segundo valor: '))

        resultado = subtracao(valor1, valor2)
        print('----------------------------------------')
        print(f'O resultado da subtração é: {resultado}')
        print('----------------------------------------')
        continue
    if escolha == 5:
        valor1 = int(input('Digite o primeiro valor: '))

        resultado = raiz(valor1)
        print('-----------------------------------')
        print(f"O resultado da raiz é: {resultado}")
        print('-----------------------------------')
        continue

    if escolha == 6:
        valor1 = int(input('Digite o primeiro valor: '))
        valor2 = int(input('Digite o número a qual será elevado: '))
        
        if valor2 == 2:
            resultado = elevacao(valor1,valor2)
            print('-----------------------------------')
            print(f"O resultado da elevação ao quadrado é: {resultado}")
            print('-----------------------------------')
            continue

        if valor2 == 3:
            resultado = elevacao(valor1,valor2)
            print('-----------------------------------')
            print(f"O resultado da elevação ao cubo é: {resultado}")
            print('-----------------------------------')
            continue

        else:
            resultado = elevacao(valor1,valor2)
            print('-----------------------------------')
            print(f"O resultado da elevação é: {resultado}")
            print('-----------------------------------')
            continue
    if escolha == 0:
        print('Obrigado por usar nosso app. :)')
        break
    else:
        print('Escolha inválida. Por favor, digite 1 para fazer uma soma.')

