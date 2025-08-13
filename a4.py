# Variáveis
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
# (3 ^ 2 + 4 ^ 2) ^ 0.5 = (9 + 16) ^ 0.5 = 25 ^ 0.5 = √25 = 5
print(f'1) O valor de c é: {c}\n')

# Desafio
km = float(input('Digite em km: '))
milhas = float(input('Digite em milhas: '))

milhas_para_km = milhas * 1.61
km_para_milhas = km / 1.61

print(f'1) As {milhas} milhas, convertidas são {km} km.\n   Já os {km} km, são {milhas} milhas.\n')

# Atribuição Composta
var = 2
var += 5 * 2
var /= 2
var **= 2
var %= 3
print(f'2) Resultado: {var}\n') # 0
