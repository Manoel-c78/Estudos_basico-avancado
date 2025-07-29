#Codigo do produto

cod = input("Digite o código do produto que deseja acessar: ")

def cod_produto(cod):
    if cod == "001":
        print("001 - Sabão")
    
    elif cod == "002":
        print("002 - Vassoura")

    elif cod == "003":
        print("003 - Detergente")

cod_produto(cod)