'''Ordenação de uma lista por meio do método sort()'''

carros = ["BMW", "Toyota", "Corsa", "Gol", "D20"]

carros.sort()
print(carros) # Impressão da lista ordenada alfabeticamente

# Se for acresentado o paramentro recerse=True, no método sorte ele ordena de forma inversa

carros.sort(reverse=True)
print(carros) # Lista impressa ordenada inversamente


#OBS: Esse método altera de forma permanente a ordem da lista