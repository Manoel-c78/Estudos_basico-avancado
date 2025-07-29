#Primeiro teste de API

import requests

url = "https://jsonplaceholder.typicode.com/todos"

print("Fazendo o pedido para a API...")
resposta = requests.get(url)

print("Código de Status da resposta:", resposta.status_code)

if resposta.status_code == 200:
    dados = resposta.json()

    print("\n--- DADOS DA PRIMEIRA TAREFA ---")
    print(dados[0])
else:
    print("Ops! A requisição falhou.")
