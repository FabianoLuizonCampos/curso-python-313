# IF / ELIF / ELSE

idade = int(input("Digite sua idade: "))

if idade < 12:
    print("Olá você é uma criança")
elif idade >= 13 and idade <= 18:
    print("Você é uma adolecente!!")
elif idade >= 19 and idade <= 30:
    print("Você é um jovem adulto")
elif idade >= 31 and idade <= 60:
    print("Você já é uma pessoa responsavel")
else:
    print("Você entrou na melhor idade")