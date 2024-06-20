# Escrita de Arquivos
def main():

    # Abrir o arquivo para escrita - a - append
    # arquivo = open("texto.txt", "a+")

    # Abrir o arquivo limpando o que esta dentro - w - write
    arquivo = open("texto.txt", "w+")

    arquivo.write("SENAI")

    arquivo.close()

if __name__ == "__main__":
    main()