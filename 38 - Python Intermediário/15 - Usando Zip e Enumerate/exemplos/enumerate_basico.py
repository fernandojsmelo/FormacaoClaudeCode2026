tarefas = ["estudar", "treinar", "revisar"]

for i, tarefa in enumerate(tarefas):
    print(i, tarefa)

for n, tarefa in enumerate(tarefas, start=1):   # começa em 1
    print(f"{n}. {tarefa}")

print(list(enumerate("ab")))
