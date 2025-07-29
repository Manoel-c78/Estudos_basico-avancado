#Calculo salário familia

salario = float(input("Digite o salário do funcionário: "))
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas: "))
filhos = int(input("Quantos filhos menores de 14 anos o funcionário possui? "))

def calculo_salario(salario):
    if salario <= 500:
        print(f"Salário bruto: R${salario:.2f} // Salário familia: R${filhos*10.50:.2f}")

    elif salario > 500 and salario <= 1000:
        print(f"Salário bruto: R${salario:.2f} // Salário familia: R${filhos*6.50:.2f}")

    elif salario > 1000:
        print(f"Salário bruto: R${salario:.2f} // Salário familia: R${filhos*1.50:.2f}")

calculo_salario(salario)
