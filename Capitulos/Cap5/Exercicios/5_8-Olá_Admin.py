'''
5.8 – Olá admin: Crie uma lista com cinco ou mais nomes de usuários, incluindo
o nome 'admin'. Suponha que você esteja escrevendo um código que exibirá
uma saudação a cada usuário depois que eles fizerem login em um site.
Percorra a lista com um laço e mostre uma saudação para cada usuário: • Se o
nome do usuário for 'admin', mostre uma saudação especial, por exemplo, Olá
admin, gostaria de ver um relatório de status?

'''

usuarios = ["admin", "Professor", "Aluno", "Gestor", "Suporte"]

for users in usuarios:
    if users == "admin":
        print(f"Olá {users}, gostaria de ver um relatório de status?\n")
    else:
        print("Seja bem vindo usuário aleatório")