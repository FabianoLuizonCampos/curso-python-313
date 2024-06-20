# Escrita de Arquivos
def main():
 
    pessoas = ["Ana", "Joao", "Bia", "Jose"]
    salarios = [5000, 2300, 6200, 9000]

    arquivo = open("texto.csv", "w+")

    # Arquivo CSV - Excel
    arquivo.write("Nome;Salario\n")
    for i in range(4):
        arquivo.write(pessoas[i])
        arquivo.write(";")
        arquivo.write(str(salarios[i]))
        arquivo.write("\n")
    

    arquivo.close()

if __name__ == "__main__":
    main()