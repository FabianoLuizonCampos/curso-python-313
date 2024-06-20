def main():
    try:
        valor = int(input("Digite um numero: "))
        resultado = 10 / valor
    except Exception as e:
        print(f"ERRO: ENTRE EM CONTATO COM O SUPORTE E PASSE A MENSAGEM ABAIXO")
        print(f"MENSAGEM: {e}")
    else:
        print("Resultado: ", resultado)

    print("Fim de Programa")



if __name__ == "__main__":
    main()