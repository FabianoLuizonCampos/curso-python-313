# OS - Operating System ou Sistema Operacional
# Pastas (Diretorios)
# Locais (Caminhos / PATH)

import os

from datetime import date

def main():

    diretorio = "E:\\Temp"

    arquivos = os.listdir(diretorio)

    for arq in arquivos:
        print(arq)

    # nova_pasta = "E:/Temp/Python313"
    # Cria uma nova pasta/diretorio
    data_hoje = str(date.today())
    nova_pasta = "E:/Temp/" + data_hoje
    #nova_pasta = "E:/Temp/2024-05-17"
    os.makedirs(nova_pasta)

    

if __name__ == "__main__":
    main()