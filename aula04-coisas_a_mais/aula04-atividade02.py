notaA = float(input("Digite a primeira nota: "))
while notaA < 0 or notaA > 10:
    print("A nota deve estar entre 0 e 10")
    notaA = float(input("Digite a nota novamente: "))

notaB = float(input("Digite a segunda nota: "))
while notaB < 0 or notaB > 10:
    print("A nota deve estar entre 0 e 10")
    notaB = float(input("Digite a nota novamente: "))

media = (notaA + notaB)/2
print(media)