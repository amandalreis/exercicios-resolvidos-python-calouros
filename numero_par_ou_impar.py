#Escreva um algoritmo que retorne ao usuário se o número informado por ele é par ou ímpar. Resolva o exercício criando e chamando um método numero_par_ou_impar() que receba como parâmetro o valor int a ser analisado e retorne "O número informado é par" ou "O número informado é ímpar" (o retorno deve ser mostrado ao usuário).

def numero_par_ou_impar(numero: int):
    if (numero % 2 == 0):
        return f"O número {numero} é par."
    else:
        return f"O número {numero} é ímpar"

print("Vamos descobrir se um número é par ou ímpar.")

numero = int(input("Digite o número a ser analisado: "))

print(numero_par_ou_impar(numero))