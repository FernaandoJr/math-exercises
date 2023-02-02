# Seno, Cosseno e Tangente:
# Escreva um programa que peça ao usuário para inserir um número em graus
# e calcule e imprima o valor do seno, cosseno e tangente desse número.]
import math

num = int(input("Insira um número em graus e irei calcular o seno, cosseno e tangente do mesmo: "))

degree = math.radians(num)
sin = math.sin(degree)
cos = math.cos(degree)
tan = math.tan(degree)

print(f"Seno de {num}° = {sin}")
print(f"Cosseno de {num}° = {cos}")
print(f"Tangente de {num}° = {tan}")


