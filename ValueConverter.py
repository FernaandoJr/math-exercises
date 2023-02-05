# Crie um conversor de moedas. O programa deve permitir que o usuário insira um valor
# em uma moeda específica e exiba o equivalente em outras moedas.

from forex_python.converter import CurrencyRates

cr = CurrencyRates()

# Conversão de EUR para USD
amount = 100.0
converted_amount = cr.convert('EUR', 'USD', amount)
print(f'{amount} EUR = {converted_amount} USD')
