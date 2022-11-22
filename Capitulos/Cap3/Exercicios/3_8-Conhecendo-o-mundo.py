''': Pense em pelo menos cinco lugares do mundo que você gostaria de visitar.
• Armazene as localidades em uma lista. Certifique-se de que a lista não esteja em ordem alfabética.
'''
lugares = ["Islândia", "Japão", "China", "Grécia", "Roma"]
'''
• Exiba sua lista na ordem original. Não se preocupe em exibir a lista de forma
elegante; basta exibi-la como uma lista Python pura.
'''

print(lugares)

'''
• Utilize sorted() para exibir sua lista em ordem alfabética, sem modificar a
lista propriamente dita.
'''

print(sorted(lugares))


#• Mostre que sua lista manteve sua ordem original exibindo-a.

print(lugares)

#• Utilize sorted() para exibir sua lista em ordem alfabética inversa sem alterar a ordem da lista original.
lugares.reverse()

print(sorted(lugares))

#• Mostre que sua lista manteve sua ordem original exibindo-a novamente.

print(lugares)

#• Utilize reverse() para mudar a ordem de sua lista. Exiba a lista para mostrar que sua ordem mudou.

lugares.reverse()

print(lugares)

#• Utilize reverse() para mudar a ordem de sua lista novamente. Exiba a lista para mostrar que ela voltou à sua ordem original.

lugares.reverse()

print(lugares)

#• Utilize sort() para mudar sua lista de modo que ela seja armazenada emordem alfabética. Exiba a lista para 
# mostrar que sua ordem mudou.

lugares.sort()
print(lugares)

#• Utilize sort() para mudar sua lista de modo que ela seja armazenada em ordem alfabética inversa. Exiba a lista 
# para mostrar que sua ordem mudou.'''

lugares.sort(reverse=True)