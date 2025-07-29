#Soma dos números de 1 até 100
n1 = 1
soma_total = 0

def soma_1_ate_100_corrigida (n1):
    global soma_total
    while n1 <= 100:
        soma_total += n1
        n1 += 1

    print(f"A soma dos números de 1 a 100 é: {soma_total}")

soma_1_ate_100_corrigida(n1)