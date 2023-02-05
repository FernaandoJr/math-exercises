# Crie um programa que gere uma lista de números aleatórios e ordene-os usando um algoritmo de ordenação,
# como o bubble sort ou o quick sort.

import random

random_list = []
tamanho = random.randint(10, 30)

for i in range(tamanho):
    random_number = random.randint(1, 100)
    random_list.append(random_number)


def bubble_sort(list):
    n = len(list)

    for i in range(n):
        for j in range(0, n - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list


print(f"Lista não ordenada:")

print(random_list)

bubble_sort(random_list)

print("")
print(f"Lista ordenada:")

print(random_list)

