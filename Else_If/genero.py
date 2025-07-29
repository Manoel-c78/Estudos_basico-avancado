#Revisão

nome = input("Qual o seu nome? ")
genero = input("Qual o seu sexo? ")


def sexo(nome, genero):
    if genero == "Masculino":
        print("Ilmo. Sr.",nome)
    elif genero == "Feminino":
         print("Ilma. Sra.",nome)

print({sexo(nome, genero)})
        