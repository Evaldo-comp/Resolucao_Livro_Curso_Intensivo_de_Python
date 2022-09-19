'''Crie uma lista de números de um a um milhão e, em seguida, use min()
e max() para garantir que sua lista realmente começa em um e termina em um
milhão. Além disso, utilize a função sum() para ver a rapidez com que Python é
capaz de somar um milhão de números.
'''

milhao = [i  for i in range  (1, 10000001)]

print(f"MINIMO: {min(milhao)}")
print(f"MÁXIMO: {max(milhao)}")
print(f"SOMA: {sum(milhao)}")