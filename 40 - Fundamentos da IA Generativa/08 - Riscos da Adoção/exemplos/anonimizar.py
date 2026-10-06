import re


def cpf_valido(cpf):
    nums = [int(c) for c in cpf if c.isdigit()]
    if len(nums) != 11 or len(set(nums)) == 1:
        return False
    for i in (9, 10):
        soma = sum(n * (i + 1 - k) for k, n in enumerate(nums[:i]))
        if (soma * 10 % 11) % 10 != nums[i]:
            return False
    return True


def anonimizar(texto):
    def troca_cpf(m):
        return "[CPF]" if cpf_valido(m.group()) else m.group()

    texto = re.sub(r"\b\d{3}\.?\d{3}\.?\d{3}-?\d{2}\b", troca_cpf, texto)
    texto = re.sub(r"[\w.+-]+@[\w-]+\.[\w.]+", "[E-MAIL]", texto)
    texto = re.sub(r"\(?\b\d{2}\)?\s?9?\d{4}-?\d{4}\b", "[TELEFONE]", texto)
    return texto


msg = ("Oi, sou a Ana (CPF 529.982.247-25), meu e-mail e "
       "ana@exemplo.com.br e o telefone (11) 91234-5678. "
       "O pedido 123.456.789-00 chegou quebrado.")
print("antes: ", msg)
print("depois:", anonimizar(msg))
