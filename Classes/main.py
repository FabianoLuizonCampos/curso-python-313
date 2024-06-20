import carro
# do arquivo carro.py a classe Carro
from carro import Carro

def main():

    # instanciar um objeto (criar)
    carro1 = Carro("Toyota", "Etios" )
    carro2 = Carro("VW", "UP")

    carro1.imprimirDados()
    carro2.imprimirDados()

    carro3 = Carro("FIAT", "UNO")
    carro_presidente = Carro("Volvo", "C40")

    

if __name__ == "__main__":
    main()