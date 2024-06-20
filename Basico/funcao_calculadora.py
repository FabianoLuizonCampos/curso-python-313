# Exercício Funções
# Criar as funções main() e as demais funções para criar uma
# calculadora com as operações +, -, /, * .
# As funções deverão realizar somente o calculo
# O usuário devera digitar 2 números e a operação que deseja realizar
# OBS.: seu código deverá bloquear a divisão por zero

# Criar as funções para calculo
def somarNumeros(n1, n2):
    res = n1 + n2
    return res
    
def subtrairNumeros(n1, n2): 
    res = n1 - n2
    return res

def multiplicarNumeros(n1, n2):
    res = n1 * n2
    return res

def dividirNumeros(n1, n2):   
    res = n1 / n2
    return res

def main():
 
    print("Olá, bem vindo a Calculadora SENAI")
    num1 = int(input("Digite o primeiro numero para calculo"))
    num2 = int(input("Digite o segundo numero para calculo"))
    operacao = input("Digite a operacao a ser calculada")

    if operacao == "+":
        resultado = somarNumeros(num1, num2)
        print(f"O valor da soma e {resultado}")
    elif operacao == "-":
        resultado = subtrairNumeros(num1, num2)
        print(f"O valor da subtracao e {resultado}")
    elif operacao == "*":
        resultado = multiplicarNumeros(num1, num2)
        print(f"O valor da multiplicacao e {resultado}")
    elif operacao == "/":
        if num2 != 0:
            resultado = dividirNumeros(num1, num2)
            print(f"O valor da divisao e {resultado}")
        else:
            print("Não existe divisao por ZERO!!!")
    else:
        print("Operacao Invalida!!!")


    
if __name__ == "__main__":
    main()

