# Escreva um algoritmo que retorne ao usuário a área de um triângulo a partir da base b e da altura h que ele informar. Resolva o exercício criando e chamando um método calcular_area_triangulo() que receba como parâmetros os valores float da base e da altura do triângulo e retorne a área (o retorno deve ser mostrado ao usuário).

def calcular_area_triangulo(base: float, altura: float):
    return (base * altura) / 2

print("Vamos descobrir a área de um triângulo.")

base = float(input("Digite o comprimento da base do triângulo: "))
altura = float(input("Digite o comprimento da altura do triângulo: "))

area = calcular_area_triangulo(base, altura)

print(f"A área do triângulo é {area}")