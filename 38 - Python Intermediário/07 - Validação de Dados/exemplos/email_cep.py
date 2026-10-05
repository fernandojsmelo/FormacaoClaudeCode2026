import re

EMAIL = re.compile(r"[\w.+-]+@[\w-]+(\.[\w-]+)+")
CEP = re.compile(r"\d{5}-?\d{3}")

for e in ["ana@site.com", "bia@site",
          "caio @x.com", "d@x.com.br"]:
    print(f"{e:13} ->", bool(EMAIL.fullmatch(e)))
for c in ["01310-100", "01310100", "1310-100"]:
    print(f"{c:13} ->", bool(CEP.fullmatch(c)))
