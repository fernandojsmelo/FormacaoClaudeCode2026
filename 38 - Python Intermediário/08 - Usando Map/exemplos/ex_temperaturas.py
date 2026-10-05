celsius = [-5, 0, 21.5, 37, 100]


def para_fahrenheit(c):
    return c * 9 / 5 + 32


fahrenheit = map(para_fahrenheit, celsius)
for c, f in zip(celsius, fahrenheit):
    print(f"{c:>6} °C = {f:>6.1f} °F")
