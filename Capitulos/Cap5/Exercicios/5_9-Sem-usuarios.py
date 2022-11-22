'''
5.9 – Sem usuários: Acrescente um teste if em hello_admin.py para garantir
que a lista de usuários não esteja vazia.
• Se a lista estiver vazia, mostre a mensagem Precisamos encontrar alguns
usuários!
• Remova todos os nomes de usuário de sua lista e certifique-se de que a
mensagem correta seja exibida.


'''

usuarios = ["admin", "Professor", "Aluno", "Gestor", "Suporte"]

if usuarios: #uma lista testa verdadeiro se tiver pelo menos 1 item, caso contrário irá retornar false
    for users in usuarios:
        if users == "admin":
            print(f"Olá {users}, gostaria de ver um relatório de status?\n")
        else:
            print("Seja bem vindo usuário aleatório")
else:
    print("Precisamos encontrar alguns usários")