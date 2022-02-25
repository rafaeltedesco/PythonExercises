# Desafio: Obter a lista e a contagem de números pares entre dois números informados pelo usuário

def get_even_numbers(a: int, b: int):
    if a == b:
        return []
    first_number, last_number = (a, b) if a < b else (b, a)
    evens = [i for i in range(first_number + 1, last_number) if i % 2 == 0]
    return {'evens': evens, 'count': len(evens)}


a, b = list(
    map(int, input("Digite dois números separados por espaço: ").split(" ")))
print(get_even_numbers(a, b))
