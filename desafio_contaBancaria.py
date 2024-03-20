mensagem = f"""Informe qual operação bancária deseja utilizar
    1 - Depositar     3 - Extrato
    2 - Sacar         4 - Encerrar Operação
"""
print(mensagem)
operacao_bancaria = int(input(": "))

while True:
    saldo = 0;
    limite = 500;
    extrato = []
    numero_saques = 0
    LIMITE_SAQUES = 3

    #depositar
    if operacao_bancaria == 1:
        valor_deposito = float(input("Informe o valor do depósito: "))

        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
            print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso.")
            print(f"Novo Saldo R$ {saldo:.2f}")

        else:
            print("Operação falhou! O valor informado é inválido.")

# Sacar
    if operacao_bancaria == 2:
        while True:
            valor_saque = float(input("Informe o valor do saque: "))

            excedeu_saldo = valor_saque > saldo
            excedeu_limite = valor_saque > limite
            excedeu_saques = numero_saques >= LIMITE_SAQUES

            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")

            elif excedeu_limite:
                print("Operação falhou! O valor do saque excede o limite.")

            elif excedeu_saques:
                print("Operação falhou! Número máximo de saques excedido.")

            elif valor_saque > 0:
                print(f"Confirma o valor {valor_saque:.2f}? (S/N)")
                confirma_saque = input().upper()
            
                if confirma_saque == 'S':
                    saldo -= valor_saque
                    extrato += f"Saque: R$ {valor_saque:.2f}\n"
                    numero_saques+=1
                    print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso.")
                    print(f"Novo Saldo: R$ {saldo:.2f}")
                    
                    if numero_saques > LIMITE_SAQUES:
                        break
                else:
                    print("Operação de saque cancelada. Informe um novo valor de saque.")
            else:
                print("Operação falhou! Saldo insuficiente ou valor inválido.")
                break  # Sai do loop se a operação falhou

#Extrato
    if operacao_bancaria == 3:
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
        break
#Sair    
    if operacao_bancaria == 4:
        print("Obrigado por utilizar nosso banco!")
        break

   

          
          
        