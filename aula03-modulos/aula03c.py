#Programa que recebe a escolha do usuário
#escolha_usuário
# 0 --> sair do programa
# 1 --> entrar no programa
#---> erro!

escolha_usuario = 0

match escolha_usuario:
    case 0:
        print("Sair do Programa")
    case 1:
        print("Entrar do Programa")
    case _:
        print("Erro!!")
