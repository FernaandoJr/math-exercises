# FizzBuzz: Escreva um programa que imprima os números de 1 a 100,
# mas para múltiplos de 3 imprima "Fizz" em vez do número e para múltiplos
# de 5 imprima "Buzz". Para números que são múltiplos de ambos (3 e 5),
# imprima "FizzBuzz".

num = 1

while num <= 100:
    if(num % 3 == 0) and (num % 5 == 0 ):
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
    num += 1;