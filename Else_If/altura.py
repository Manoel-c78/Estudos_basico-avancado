#Altura

altura = float(input("Digite a sua altura: "))
sexo = input("Digite o seu sexo: (M ou F) ")

def pesoIdeal(altura):
    if sexo == "F":
        return (62.1*altura) - 44.7
    elif sexo == "M":
        return (72.7*altura) - 58

    
print(f"O seu peso ideal é de aproximadamente: {pesoIdeal(altura):.2f}")