# Calculadora: Escreva um programa que peça ao usuário
# para inserir dois números e um operador (+, -, *, /).
# O programa deve calcular e imprimir o resultado da operação.

print("Insira números para serem calculados")
n1 = int(input("Número 1: "))
n2 = int(input("Número 2: "))

print("Insira um operador para ser usado (+, -, *, /)")
op = (input("Operador escolhido: "))

if op == "+":
    resultado = n1 + n2
    print(f"Resultado de {n1} {op} {n2} = {resultado}")
elif op == "-" :
    resultado = n1 - n2
    print(f"Resultado de {n1} {op} {n2} = {resultado}")
elif op == "*" :
    resultado = n1 * n2
    print(f"Resultado de {n1} x {n2} = {resultado}")
elif op == "/" :
    resultado = n1 / n2
    print(f"Resultado de {n1} {op} {n2} = {resultado}")
else:
    print("Nenhum operador válido foi escolhido")