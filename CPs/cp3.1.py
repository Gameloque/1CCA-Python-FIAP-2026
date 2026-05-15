temp = [[28, 31, 34, 33],
        [25, 27, 29, 28],
        [32, 35, 36, 34],
        [24, 26, 25, 27]]

med = [0, 0, 0, 0]
for i in range(0,4):
    crt = [0,0,0,0]
    for j in range(0,4):
        if temp[i][j] >= 33:
            crt[i] += 1
        med[i] += temp[i][j]

    print()
    print(f"Sala {i + 1}\nMedia:{med[i] / 4}")
    print(f"Registro Critico: {crt[i]}")
    if crt[i] > crt[i-1]:
        valorCrt = i + 1

