# Números primos: Escreva um programa que determine se um número é primo ou não.

num = int(input("Digite um número para verificar se é primo ou não: "))

if num < 2:
    print(f"{num} não é primo")

for i in range(2, num):
    if num % i == 0:
        print(f"{num} não é primo")
        break
else:
    print(f"{num} é primo")
