# ----------> Desafio 9
# Fazer um programa para o usuario digitar 2 numeros sendo o 
# primeiro menor que o segundo e mostrar os numeros pares 
# entre esses 2 numeros
# Dica: utilizar o operador de resto - % - para descobrir
# se o numero é par

num1 = int(input("Digite o primeiro numero do intervalo: "))
num2 = int(input("Digite o segundo numero do intervalo: "))

if num1 > num2:
    num1 , num2 = num2 , num1

while num1 <= num2:
    if (num1 % 2) == 0:
        print(num1)

    num1 = num1 + 1