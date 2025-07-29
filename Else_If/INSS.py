#INSS

salario = float(input("Digite o salário do funcionário: "))

def INSS(salario):
    if salario <= 500:
        print(f"Salário: R${salario:.2f}, Taxa: 8%, Valor do INSS: R${salario*0.08:.2f}, Salário líquido: R${salario-(salario*0.08):.2f}")

    elif salario > 501 and salario <= 1000:
        print(f"Salário: R${salario:.2f}, Taxa: 10%, Valor do INSS: R${salario*0.1:.2f}, Salário líquido: R${salario-(salario*0.1):.2f}")

    elif salario > 1000:
        print(f"Salário: R${salario:.2f}, Taxa: 12%, Valor do INSS: R${salario*0.12:.2f}, Salário líquido: R${salario-(salario*0.12):.2f}")

INSS(salario)        