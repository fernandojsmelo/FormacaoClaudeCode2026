cores = ["azul", "verde", "azul", "rosa"]
print("verde" in cores)      # True
print(cores.index("azul"))   # 0: primeira posição
print(cores.count("azul"))   # 2
for i, cor in enumerate(cores):
    print(i, cor)
