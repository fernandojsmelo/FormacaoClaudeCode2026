with open("registros.bin", "wb") as f:
    for i in range(5):
        f.write(f"REG{i:02d}".encode())  # registros de 5 bytes

with open("registros.bin", "rb") as f:
    print(f.read(5), f.tell())        # leu 5: posição 5
    f.seek(3 * 5)                     # pula para o 4º
    print(f.read(5), f.tell())
    f.seek(-5, 2)                     # 5 bytes antes do fim
    print(f.read())
