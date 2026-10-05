ponto = (3, 4)
cores = ("vermelho", "verde", "azul")
sem_parenteses = 10, 20        # a vírgula é que cria a tupla
um_item = ("só",)  # um item: precisa da vírgula
nao_e_tupla = ("só")  # sem vírgula: é só uma str
print(type(sem_parenteses), type(um_item), type(nao_e_tupla))
print(cores[0], cores[-1], cores[1:])
print(len(cores), "verde" in cores)
