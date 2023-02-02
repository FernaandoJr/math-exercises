# Tabuada: Escreva um programa que peça ao usuário para inserir um número e imprima sua tabuada (1 a 10).

num = int(input("Insira um número e te mostrarei a tabuada do mesmo (1 a 10): "))

for i in range (1,11):
    resultado = num * i

    print(f"{num} x {i} = {resultado}")