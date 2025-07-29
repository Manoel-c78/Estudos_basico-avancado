#Descobrir idade pelo ano de nascimento

ano = int(input("Digite o ano de seu nascimento: "))

def verificacao (ano):
    return 2025 - ano

idade = verificacao(ano)

if idade < 18:
    print("Você pode votar, MAS, não pode tirar habilitação")

elif idade >= 18:
    print("Você pode votar e tirar habilitação")

else:
    print("Você não pode votar e também não pode tirar habilitação")

print(idade)