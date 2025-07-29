#Soma Fibonacci até o 10º termo - Versão Corrigida
n1 = 0
n2 = 1
soma_total = 0
sequencia = 1

def soma_Fibonacci_corrigida (n1_param, n2_param):
   global soma_total
   global sequencia
   
   if sequencia == 1:
       soma_total += n1_param
       print(f"Termo {sequencia}: {n1_param}")
       sequencia += 1
   if sequencia == 2:
       soma_total += n2_param
       print(f"Termo {sequencia}: {n2_param}")
       sequencia += 1

   while sequencia <= 10:
       n3 = n1_param + n2_param
       print(f"Termo {sequencia}: {n3}")
       soma_total = soma_total + n3 

       n1_param = n2_param
       n2_param = n3

       sequencia += 1 

soma_Fibonacci_corrigida(n1, n2)