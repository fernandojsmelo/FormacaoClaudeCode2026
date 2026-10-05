def media(notas: list[float]) -> float:
    return sum(notas) / len(notas)


def saudacao(nome: str) -> str:
    return "Olá, " + nome


media(["8", "9"])              # strings em vez de números
saudacao(42)                   # int em vez de str
total: int = media([7.0, 8.0])  # float guardado como int
