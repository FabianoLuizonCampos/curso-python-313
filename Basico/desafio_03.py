# Desafio 03
# Desenvolver um programa para uma loja de lanches (MAC)
# Requisitos:
# - O usuário vai receber uma mensagem de boas vindas
# - O sistema irá pedir qual seria a opção de lanche (Nº1, ...)
# - O sistema irá retornar o nome lanche e o valor dele
# - Usar pelo menos 4 opções de lanche
# - Para resolver usar listas  

# lanches = {
#     "1": ["Calabresa", "R$19.99"],
#     "2": ["Frango", "R$22.99"],
#     "3": ["Churrasco", "R$30.99"]
# }

# opcao = (input("Numero:"))

# print("Seu lanche eh: ", lanches[opcao][0], " e o preco eh: ", 
#         lanches[opcao][1] )

lista_de_lanches = ["BIG MAC", "CHEEDAR MAC MELT", "QUARTEIRAO", "BIG TASTY"]
lista_de_precos = [29.99, 27.90, 18.50, 35.60]

print("--------- BEM VINDO AO MAC SENAI MAUA -----------")
opcao = int(input("Digite sua opcao de lanche (1 à 4):"))

print("Seu lanche escolhido foi ", lista_de_lanches[opcao - 1])
print("O valor do lanche é R$", lista_de_precos[opcao - 1])