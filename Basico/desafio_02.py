# Cálculo da Área do Círculo
# O programa deverá calcular a área do círculo utilizando
# o raio que o usuário vai digitar.

# CONSTANTE (Nome é em letras maiusculas (padrao))
PI = 3.1415

print("-----------Cálculo da Área do Círculo-----------------")
raio = float(input("\nDigite o raio do círculo: "))

area = PI * (raio ** 2)

print("\nO valor da área do círculo é ", area)
print(f"\nO resultado foi {area} da área do círculo")