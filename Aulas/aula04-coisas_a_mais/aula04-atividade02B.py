def val_nota(nota):
    while nota < 0 or nota > 10:
        print("A nota deve estar entre 0 e 10")
        nota = float(input("Digite a nota novamente: "))
    return nota

notaA = float(input("Digite a primeira nota: "))
notaA = val_nota(notaA)

notaB = float(input("Digite a segunda nota: "))
notaB = val_nota(notaB)

media = (notaA + notaB)/2
print(media)