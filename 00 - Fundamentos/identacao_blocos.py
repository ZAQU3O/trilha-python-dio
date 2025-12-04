saldo = 500

def sacar(valor):
    global saldo

    if saldo >= valor:
        print("valor sacado!")
        print("retire o seu dinheiro na boca do caixa.")

    print("Obrigado por ser nosso cliente, tenha um bom dia!")


def depositar(valor):
    global saldo
    saldo += valor

    print(f"Depósito de R$ {valor} realizado com sucesso!")
    print(f"Seu saldo atual é R$ {saldo}")

def extrato():
    global saldo
    print(f'''
    ******* EXTRATO *******
    
    SALDO: R$ {saldo}
    ************************
    ''')


sacar(1000)
extrato()
depositar(500)
extrato()