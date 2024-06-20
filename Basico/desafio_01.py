# Desafio 01 - Cálculo do IMC
# Desenvolver um programa que calcule o IMC da pessoa:
# Requisitos:
# - Peso e altura da pessoa será digitado pelo teclado (Dica: usar input() )
# - O pessoa vai se identificar através do nome (Dica: usar input() ),
# - Realizar o cálculo padrão do IMC (Dica: usar operadores aritmeticos e variaveis)
# - Apresentar o resultado na tela com o Nome e o Valor do IMC (Dica: usar print() com 
#       formatação print(f"") e as variaveis)

#Texto
nome = input("Olá, qual é seu nome: ")

#Número Reais
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

imc = peso / (altura ** 2)
imc = round(imc, 2)

print(f"{nome} seu IMC é {imc}")