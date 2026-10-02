# vetor_teste = [100, 2, 4.79]
# vetor_teste.append("Cuscuz")
# vetor_teste.append("tomate")
# vetor_teste.append("suco")
# vetor_teste.append("banana")
#
#
# print(vetor_teste)
# print()
# tamanho = len(vetor_teste)
# for i in range(tamanho):
#     print(vetor_teste[i])
#
# print()
#
# for teste in vetor_teste:
#     print(teste)
#
# print()
#
# msg = "Helo"
#
# for i in range(len(msg)):
#     print(msg[i])
#

nomes = ["João", "Bob", "Ana", "Joel"]

for i in range(len(nomes)):
    for j in range(i+1, len(nomes)):
        print(f'Duplas: {nomes[i]}, {nomes[j]}')




