def eh_primo(n):
    if n < 2:
        return False
    return all(n % d != 0 for d in range(2, int(n ** 0.5) + 1))


print(list(filter(eh_primo, range(1, 30))))

codigos = ["123", "ab1", "007", "", "4 5"]
print(list(filter(str.isdigit, codigos)))   # método pronto
