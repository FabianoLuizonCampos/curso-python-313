import os
# pip install pypdf2
import PyPDF2

def main():
    
    merger = PyPDF2.PdfMerger()

    lista_arquivos = os.listdir("Arquivos") 
    lista_arquivos.sort()
    print(lista_arquivos) 

    for arquivo in lista_arquivos:
        if ".pdf" in arquivo:
            merger.append(f"Arquivos/{arquivo}")

    merger.write("Arquivos/PDF_Final.pdf")

if __name__ == "__main__":
    main()