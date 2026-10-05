def media(notas: list[float]) -> float:
    return sum(notas) / len(notas)


def por_aluno(
    registros: list[tuple[str, float]],
) -> dict[str, float]:
    return {nome: nota for nome, nota in registros}


tags: set[str] = {"python", "tipos"}
print(media([7.5, 9.0, 8.0]))
print(por_aluno([("ana", 9.5), ("bia", 8.0)]))
print(sorted(tags))
