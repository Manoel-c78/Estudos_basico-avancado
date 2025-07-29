#Desconto de produtos

valor = float(input("Digite o valor do produto: "))

def desconto(valor):
    return valor - (valor*0.09)

print(f"O valor do produto pós desconto ficou no valor de: R${desconto(valor):.2f} ")