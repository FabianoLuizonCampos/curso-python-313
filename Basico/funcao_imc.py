# Módulo de Calculo do IMC
def calcularIMC(altura, peso):

    imc = peso / (altura ** 2)

    return imc

# Módulo de Mensagem ao usuario do IMC
def imprimirIMC(imc):

    print(f"Olá usuario, seu IMC é {imc}!!!")

# Módulo de Mensagem de boas vindas
def imprimirBoasVindas():

    print("********* SISTEMA DE CÁLCULO DO IMC *********")
    print("Olá, seja bem vindo ao sistema de cálculo do IMC")

# Módulo Principal
def main():

    imprimirBoasVindas()
    
    resultado = calcularIMC(1.80, 88)
    resultado = round(resultado,2)

    imprimirIMC(resultado)


if __name__ == "__main__":
    main()