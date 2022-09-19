quadrados =[]
for valor in range(1, 11):
    quadrado = valor ** 2
    quadrados.append(quadrado)
    print(quadrados)

# O mesmo código a cima, só que utilizando list comprehensions

numeros = [valor ** 2 for valor in range(1, 11)]
print(numeros)