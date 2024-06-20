# Desenvolver um programa para verificar a situação do aluno
# em relação ao sua promoção escola
#   1. O aluno deverá digitar 3 notas através do teclado
#   2. Seu programa deverá calcular a média das notas    
#   3. A partir da média, verificar qual situação o aluno se encontra 
# conforme notas abaixo:
#       3.1 nota > 70 - aprovado
#       3.2 nota < 40 - reprovado
#       3.3 nota entre 40 e 70 - exame/recuperação
#   4. Não será permitido médias acima de 100 e abaixo de zero
#   5. Caso isso ocorrá o aluno deverá ser informado sobre um erro de digitação
#   6. Mostrar na tela para o aluno a situação final baseado na nota digitada.

#   7. Acrescente no desafio anterior a frequencia de no minimo 75% para ser aprovado
#   8. O aluno pode ser aprovado se ele recebeu uma dispensa da disciplina

dispensa = input("Você possui dispensa da disciplina (S/N): ")

if dispensa == "s" or dispensa == "S":
    print("Você esta aprovado por dispensa")
else:
    frequencia = int(input("Digite sua frequencia: "))

    if frequencia < 75:
        print("Você reprovou por frequencia")
    else:
        nota1 = int(input("Olá, digite sua nota1: "))
        nota2 = int(input("Digite sua nota2: "))
        nota3 = int(input("Digite sua nota3: "))       

        media = (nota1 + nota2 + nota3) / 3

        if media >= 0 and media <= 100:
            if media >= 70:
                print("APROVADO")
            elif media >= 40 and media < 70:
                print("EXAME")
            else: 
                print("REPROVADO")
        else:
            print("Media Invalida, erro de digitação")
        