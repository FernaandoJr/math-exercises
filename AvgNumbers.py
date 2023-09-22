# Média de números: Escreva um programa que peça ao usuário
# para inserir uma série de números, calcule a média dos números
# e imprima o resultado.

numbers = []

while True:
    number = input("Digite vários números para se ter uma média deles (Pressione Enter para sair): ")
    if number == "":
        break
    numbers.append(float(number))

med = sum(numbers) / len(numbers)

print(f"A média da lista é: {med}")