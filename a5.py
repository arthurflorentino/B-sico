# Cálculo da hipotenusa (c).
# Elevar a 0.5 é o mesmo que elevar a 1/2 ou a própria raiz do número.
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print(f'1) c = {c}\n')

# Retângulo
print(f'2)')
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")
print(f'\n')

# Expressão matemática
x = 5
y = 1 / (x + 1 / (x + 1 / (x + 1 / x)))
print(f'3) y = {y}\n')

# Horas
print('4) Horários do evento:')
horas = 12
min = 5
duracao = 45
min += duracao  # encontre um total de todos os minutos
horas += min // 60 # encontre um número de horas escondido em minutos e atualize a hora
min %= 60 # minutos corretos para cair no intervalo (0..59)
horas %= 24 # horas corretas para cair no intervalo (0..23)

print(f'O evendo terminará às {horas}:{min}.\n')

# Desafio com operadores de comparação
n = 55
m = 101
print(f'5)\n{n >= 100}')
print(m >= 100, '\n')
