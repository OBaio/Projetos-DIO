"""

[1] - Depósito
[2] - Saque
[3] - Extrato
[4] - Encerrar

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    menu = input("Digite uma opção: ")
    opcao = menu

    if opcao == "1":

        deposito = float(input("Digite o valor do depósito: "))

        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito: R${deposito:.2f}\n"

        else:
            print("Operação não realizada! informe um valor válido")

    elif opcao == "2":

        saque = float(input("Digite o valor do saque: "))

        excedeu_saldo = saque > saldo
        excedeu_limite = saque > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação não realizada! Você não possui saldo para essa operação")

        elif excedeu_limite:
            print("Operação não realizada! Você excedeu o limite de R$500,00 por saque")

        elif excedeu_saques:
            print("Operação não realizada! Você excedeu seu limite de 3 saques diários")

        elif saque > 0:
            saldo -= saque
            extrato += f"Saque: R${saque:.2f}\n"
            numero_saques += 1

    elif opcao == "3":
        """ EXTRATO """

        print("Nenhuma operação foi realizada" if not extrato else extrato)
        print(f"O saldo disponível em sua conta é de: {saldo}")


    elif opcao == "4":
        print("Sessão encerrada")
        break

    else:
        print("Opção invalida, tente novamente")