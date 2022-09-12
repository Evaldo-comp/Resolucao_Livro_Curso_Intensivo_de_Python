'''3.6 – Mais convidados: Você acabou de encontrar uma mesa de jantar maior, portanto agora tem mais espaço 
disponível. Pense em mais três convidados para o jantar.
• Comece com seu programa do Exercício 3.4 ou do Exercício 3.5. Acrescente uma instrução print no final de seu 
programa informando às pessoas que você encontrou uma mesa de jantar maior.

• Utilize insert() para adicionar um novo convidado no início de sua lista.
• Utilize insert() para adicionar um novo convidado no meio de sua lista.
• Utilize append() para adicionar um novo convidado no final de sua lista.
• Exiba um novo conjunto de mensagens de convite, uma para cada pessoa que está em sua lista'''

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

print(f"Por favor", convidados[0], "venha jantar conosco")
print(f"Por favor", convidados[1], "venha jantar conosco")
print(f"Por favor", convidados[2], "venha jantar conosco")
print(f"Por favor", convidados[3], "venha jantar conosco")
print(f"Por favor", convidados[4], "venha jantar conosco")
print(f"Por favor", convidados[5], "venha jantar conosco")