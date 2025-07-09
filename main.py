from datetime import datetime

menu = """
       [1] Sacar
       [2] Depositar
       [3] Consultar Extrato
       [0] Sair
       >>> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
       opcao = int(input(menu))
       if opcao == 1:
              print(f'SAQUE'.center(25, '='))
              valor = float(input("Informe o valor:\n>>> "))

              excedeu_saldo = valor > saldo
              excedeu_limite = valor > limite
              exedeu_lim_saques = numero_saques >= LIMITE_SAQUES

              if excedeu_saldo:
                     print(f'Operação não pode ser realizada! Saldo insuficiente!')
              elif excedeu_limite:
                     print(f'Operação não pode ser realizada! O limite de saque é de R$500,00')
              elif exedeu_lim_saques:
                     print(f'Operação não pode ser realizada! Limite de saques exedido!')
              elif valor > 0:
                     saldo -= valor
                     numero_saques += 1
                     extrato += f'[[{datetime.now()}]] Saque: R${valor:.2f}\n'
                     print(f'Saque realizado!')
              else:
                     print(f'A operação falhou! O valor informado é inválido!')


       elif opcao == 2:
              print(f'DEPÓSITO'.center(25, '='))
              valor = float(input(f'Informe o valor:\n>>> '))

              if valor > 0:
                     saldo += valor
                     extrato += f'[[{datetime.now()}]] Depósito: R${valor:.2f}\n'
                     print(extrato)
              else:
                     print(f'A operação falhou! O valor informado é inválido!')

       elif opcao == 3:
              print(f'EXTRATO'.center(50, '='))

              if not extrato:
                     print(f'Ainda não foram realizadas movimentações! ')
              else:
                     print(extrato)
                     print(f'>>> Saldo Total: R${saldo:.2f}')
                     print('='*50)

       elif opcao == 0:
              print(f'Encerrando o Sistema!')
              break

       else:
              print("Operação inválida, por favor selecione novamente a operação desejada.")