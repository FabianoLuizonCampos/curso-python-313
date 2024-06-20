# As maçãs custam R$0.30	 cada	 se	 forem	 compradas	menos
# do	 que	 uma dúzia,	 e	 R$	 0.25	 se	 forem	 compradas	 
# pelo menos	 doze.	 Escreva	 um	 programa	 que	 leia	 
# o	 número de	 maçãs	 compradas,	 calcule  e escreva	 o	valor	
# total	da	compra.

# CONSTANTES
VALOR_MACA_MAIOR_12 = 0.25
VALOR_MACA_MENOR_12 = 0.30

print("---------------- MAÇÃS ---------------")

qtde_macas = int(input("Quantas maçãs você deseja comprar? "))

if qtde_macas >= 12:
    print("O valor da sua compra é ", (qtde_macas * VALOR_MACA_MAIOR_12))
else:
    print("O valor da sua compra é ", (qtde_macas * VALOR_MACA_MENOR_12))