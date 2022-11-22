'''3.5 – Alterando a lista de convidados: Você acabou de saber que um de seus convidados não poderá comparecer ao 
jantar, portanto será necessário enviar um novo conjunto de convites. Você deverá pensar em outra pessoa para
convidar.
• Comece com seu programa do Exercício 3.4. Acrescente uma instrução print no final de seu programa, especificando 
o nome do convidado que não poderá comparecer.
• Modifique sua lista, substituindo o nome do convidado que não poderá comparecer pelo nome da nova pessoa que você
 está convidando.
• Exiba um segundo conjunto de mensagens com o convite, uma para cada pessoa que continua presente em sua lista.
'''
convidados = ["Ana", "Maria", "Alberto"]


print(f"Por favor", convidados[0], "venha jantar conosco")
print(f"Por favor", convidados[1], "venha jantar conosco")
print(f"Infelizmente ", convidados[2], "Não poderá comparecer")

convidados[2] = "João"

print(f"Por favor", convidados[0], "venha jantar conosco")
print(f"Por favor", convidados[1], "venha jantar conosco")
print(f"Por favor", convidados[2], "venha jantar conosco")
