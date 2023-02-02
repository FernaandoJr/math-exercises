# Adivinhe o número: Escreva um programa que gere um número aleatório entre 1 e 100
# e peça ao usuário para adivinhá-lo. O programa deve fornecer dicas (maior ou menor)
# até que o usuário adivinhe corretamente.

import random

secret = random.randint(1, 100)

num = int(input("Digite um número entre 1 - 100 e veja se este número está maior ou menor até acertá-lo: "))

while True:
    if num > secret:
        num = int(input(f"{num} é maior do que o número selecionado, tente novamente: "))
    elif num < secret:
        num = int(input(f"{num} é menor do que o número selecionado, tente novamente: "))
    else:
        print("Parabéns, você acertou o número secreto!")
        break
