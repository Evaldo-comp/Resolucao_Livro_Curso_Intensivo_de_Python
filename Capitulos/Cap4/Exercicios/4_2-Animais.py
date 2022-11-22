'''Animais: Pense em pelo menos três animais diferentes que tenham uma
característica em comum. Armazene os nomes desses animais em uma lista e,
então, utilize um laço for para exibir o nome de cada animal.
'''
from os import get_handle_inheritable


animais = ["Pato", "Galinha", "Corvo"]

for animal in animais:
    print(animal)

'''
• Modifique seu programa para exibir uma frase sobre cada animal, por
exemplo, Um cachorro seria um ótimo animal de estimação.
'''

for animal in animais:
    if animal is "Pato":
        print(f"O {animal} é muito bom nadador")
    elif animal is "Galinha":
        print(f"A {animal} é muito grande")
    else:
        print(f"O {animal} mete muito medo em algumas pessoas")

'''
• Acrescente uma linha no final de seu programa informando o que esses
animais têm em comum. Você poderia exibir uma frase como Qualquer um
desses animais seria um ótimo animal de estimação!
'''

print("Todos esses animais são aves")