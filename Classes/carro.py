class Carro:
    # Caracteristicas
    ano = 0
   
    # Método Construtor: executado automaticamente quando o objeto é criado
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        

    # Funcionalidades(funções -> métodos)
    def imprimirDados(self):
        print(f"A marca do meu carro eh {self.marca} e o modelo eh {self.modelo}")