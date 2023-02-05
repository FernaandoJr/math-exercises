# Escreva um programa que calcule a média, o desvio padrão e a mediana de uma lista de números inseridos pelo usuário.

import statistics

numbers = []
print("Digite uma Lista de Números e direi a Média Aritmética, Desvio padrão, mediana e Variância (Pressione Enter para sair): ")
while True:
    number = input("")
    if number == "":
        break
    numbers.append(int(number))

# Média
Avg = statistics.mean(numbers)

# Moda
Mode = statistics.mode(numbers)

# Desvio Padrão
DesvioP = statistics.stdev(numbers)

# Mediana
Median = statistics.median(numbers)

# Variância
Variance = statistics.variance(numbers)

# Resultados
print("")
print(f"Lista = {numbers}")
print(f"Média Aritmética: {Avg}")
print(f"Moda: {Mode}")
print(f"Desvio Padrão: {DesvioP}")
print(f"Mediana: {Median}")
print(f"Variância: {Variance}")
