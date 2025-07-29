#Peso excedente do peixe

peso = float(input("Digite o peso do peixe: "))

def calcular_taxa (peso):
    return peso - 50

multa = calcular_taxa(peso)

if multa < 50:
    print("O valor permanece sem multa a agragar.")

else:
    multa * 4
    print(f"O valor a ser pago de multa será de R${multa}:.2f")