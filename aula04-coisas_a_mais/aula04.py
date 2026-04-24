# Repetição
# cp = 0
# while cp < 3:
#     print(f"Produto {cp}")
#     cp+= 1
# print()
# Repetição contada
# i = 4
# while i > 0:
#     print(i)
#     i -= 1
# # Repetição com entrada do usuario
# jogar = "Sim"
#
# while jogar.lower() == "sim":
#     print("Inicia ou repete o jogo")
#     jogar = input("Deseja jogar novamente?")
#
# Modificadores de fluxo do laço
cp = 0
while cp < 10:
    cp += 1
    if cp == 3 or 5:
        continue
    if cp == 7:
        break

    print(f'Produto {cp}')

# # Impar e Par
# i = 0
# while i <0:
#     i+= 1
#     if i % 2 == 0:
#          continue
#     print(f'Produto  {i}')