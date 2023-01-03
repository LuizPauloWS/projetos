menu =  """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair


===> """

saldo = 5000
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        deposito = float(input("Digite o valor a ser depositado: R$ "))
        
        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f} \n"
        
        else:
            print ("Operação inválida. Insira um valor POSITIVO")
        
    elif opcao == "s":
        valor = float(input("Informe o valor a ser sacado: R$ "))
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print ("Falha na operação. Não possui saldo suficiente.")
        
        elif excedeu_limite:
            print ("Falha na operação. Valor limite de saque ultrapassado.")
            
        elif excedeu_saques:
            print ("Falha na operação. Você já antingiu a cota de 3 (três) saques diarios.")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            
        else:
            print ("Falha na operação. Valor informado inválido.")
    
    
             
    
    elif opcao == "e":
        if not extrato:
            print (f"Salto atual de: R$ {saldo:.2f}\nNenhuma movimentação registrada.")
        else:
            print (f"Salto atual de: R$ {saldo:.2f}\nHistórico de movimentação:\n{extrato}")
        
    elif opcao == "q":
        print ("Efetuando a saida do sistema\n...\n...\n...\nLoggout realizado.")
        break
