def func1():
    print("Sou a funcao 1")

def func2():
    print("Sou a funcao 2")
    print("Agora estou ativa")

def func3():
    print("Sou a funcao 3")

# FUNCAO PRINCIPAL
def main():

    func3()
    func1()

    print("Funcao Principal - Main")

    func2()
    func3()



# CONDICAO PARA EXECUTAR A FUNCAO PRINCIPAL
if __name__ == "__main__":
    main()