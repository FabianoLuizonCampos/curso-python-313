dispensa = input("Você possui dispensa da disciplina (S/N): ")

frequencia = int(input("Digite sua frequencia: "))

nota1 = int(input("Olá, digite sua nota1: "))
nota2 = int(input("Digite sua nota2: "))
nota3 = int(input("Digite sua nota3: "))       

media = (nota1 + nota2 + nota3) / 3

if dispensa != "S":

    if media >= 0 and media <= 100 and frequencia >= 75:
        if media >= 70:
            print("APROVADO")
        elif media >= 40 and media < 70:
            print("EXAME")
        else: 
            print("REPROVADO")
    else:
        print("Media Invalida ou Frenquencia abaixo de 75%")

else:
    print("APROVADO - DISPENSA")
        