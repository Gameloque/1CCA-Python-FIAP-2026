# Faça um programa que leia 3 valores que representam os lados de um triângulo A,
# B e C e ordene-os em ordem decrescente, de modo que o lado A representa o
# maior dos 3 lados. A seguir, determine o tipo de triângulo que estes três lados
# formam, com base nos seguintes casos:
# Se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO;
# Se A² = B² + C², apresente a mensagem: TRIANGULO RETANGULO;
# Se A² > B² + C², apresente a mensagem: TRIANGULO OBTUSANGULO;
# Se A² < B² + C², apresente a mensagem: TRIANGULO ACUTANGULO;
# Se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO;
# Se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO
# ISOSCELES;
lados = []
lados.append(float(input("Digite o primeiro valor: ")))
lados.append(float(input("Digite o segundo valor: ")))
lados.append(float(input("Digite o terceiro valor: ")))

lados.sort(reverse=True)

lA = lados[0]
lB = lados[1]
lC = lados[2]
print(f"Seus valores são {lA}, {lB} e {lC}.")

if lA >= lB + lC:
        print("NAO FORMA TRIANGULO")
else:
    if lA ** 2 == lB ** 2 + lC ** 2:
            print("TRIANGULO RETANGULO")
    if lA ** 2 > lB ** 2 + lC ** 2:
            print("TRIANGULO OBTUSANGULO")
    if lA ** 2 < lB ** 2 + lC ** 2:
            print("TRIANGULO ACUTANGULO")
    if lA == lB == lC:
            print("TRIANGULO EQUILATERO")
    elif lA == lB or lB == lC:
            print("TRIANGULO ISOSCELES")