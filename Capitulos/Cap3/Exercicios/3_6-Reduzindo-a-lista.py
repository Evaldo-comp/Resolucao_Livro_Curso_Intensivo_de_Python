'''3.7 – Reduzindo a lista de convidados: Você acabou de descobrir que sua nova mesa de jantar não chegará a tempo 
para o jantar e tem espaço para somente dois convidados.
• Comece com seu programa do Exercício 3.6. Acrescente uma nova linha que mostre uma mensagem informando que você 
pode convidar apenas duas pessoas para o jantar.

• Utilize pop() para remover os convidados de sua lista, um de cada vez, até que apenas dois nomes permaneçam em 
sua lista. Sempre que remover um nome de sua lista, mostre uma mensagem a essa pessoa, permitindo que ela saiba que
você sente muito por não poder convidá-la para o jantar.
• Apresente uma mensagem para cada uma das duas pessoas que continuam na lista, permitindo que elas saibam que ainda
estão convidadas.
• Utilize del para remover os dois últimos nomes de sua lista, de modo que você tenha uma lista vazia. Mostre sua 
lista para garantir que você realmente tem uma lista vazia no final de seu programa.'''

convidados = ["Ana", "Maria", "Alberto"]


print(f"Por favor", convidados[0], "venha jantar conosco")
print(f"Por favor", convidados[1], "venha jantar conosco")
print(f"Infelizmente ", convidados[2], "Não poderá comparecer")

convidados[2] = "João"

print(f"Por favor", convidados[0], "venha jantar conosco")
print(f"Por favor", convidados[1], "venha jantar conosco")
print(f"Por favor", convidados[2], "venha jantar conosco")

print(f"Gostaria de informar que encontrie uma mesa maior")

convidados.insert(0, "Renato")
convidados.insert(2, "Patricia")
convidados.append("Renata")

print(convidados)

print(f"Por favor", convidados[0], "venha jantar conosco")
print(f"Por favor", convidados[1], "venha jantar conosco")
print(f"Por favor", convidados[2], "venha jantar conosco")
print(f"Por favor", convidados[3], "venha jantar conosco")
print(f"Por favor", convidados[4], "venha jantar conosco")
print(f"Por favor", convidados[5], "venha jantar conosco")

print("Infelizmente só poderei convidar duas pessoas para o jantar ")

print(convidados.pop(),"Sinto muito mas não poderemos jantar dessa vez, fica para a próxima")
print(convidados.pop(),"Sinto muito mas não poderemos jantar dessa vez, fica para a próxima")
print(convidados.pop(),"Sinto muito mas não poderemos jantar dessa vez, fica para a próxima")
print(convidados.pop(),"Sinto muito mas não poderemos jantar dessa vez, fica para a próxima")



print(convidados[0],"Nosso jantar está de pé. Aguardo você")
print(convidados[1],"Nosso jantar está de pé. Aguardo você")

print(convidados)

del convidados[0]
del convidados[0]

print(convidados)