

def get_evens(n1: int, n2: int):
    if n1 == n2:
        return []
    n1, n2 = (n1, n2) if n1 < n2 else (n2, n1)
    return list(filter(lambda n: n % 2 == 0, range(n1 + 1, n2)))


n1, n2 = list(
    map(int, input("Digite o 1º o 2º número separado por espaço: ").split()))


evens = get_evens(n1, n2)
print(evens)
