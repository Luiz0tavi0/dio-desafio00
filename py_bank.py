# constantes
MAX_WITHDRAW = 3
MAX_WITHDRAW_VALUE = 500.00

operations = ["d", "s", "q", "e"]

bank_statement = ""  #
currency_value = 0.0
balance = 0.0
remain_withdraw = MAX_WITHDRAW

menu = """
******************************
    [d] - depositar R$
    [s] - sacar R$
    [e] - extrato bancário
    [q] - sair
******************************
"""
while True:
    choice_operation = input(menu)
    if choice_operation not in operations:
        print("Operação inválida, tente novamente.")
        continue
    if choice_operation == "e":
        if bank_statement:
            print("EXTRATO BANCÁRIO".center(30, "-"))
            print(bank_statement.center(30))
            print("SALDO: " + f" R$ {balance:.2f}".rjust(23,'.'))
        else:
            print("Não foram realizadas movimentações.")
        continue
    if choice_operation == "q":
        print("Saindo...")
        break
    currency_value = float(input("valor (R$): "))
    if currency_value <= 0:
        print(r"O valor deve ser maior que 0.00")
        continue
    if choice_operation == "s":
        if remain_withdraw == 0:
            print("Voce atingiu o limite de saques diários.")
        elif currency_value > balance:
            print("Saldo insuficiente.")
        elif currency_value > MAX_WITHDRAW_VALUE:
            print(f"O limite por saque é {MAX_WITHDRAW_VALUE:.2f}.")
        else:
            balance -= currency_value
            remain_withdraw -= 1
            bank_statement += "[\033[31mS\033[0m] - R$ " + f" {currency_value:.2f}\n".rjust(22,'.')
    else:
        balance += currency_value
        bank_statement += "[\033[32mD\033[0m] - R$ " + f" {currency_value:.2f}\n".rjust(22,'.')
