def is_palindrome_solution1(characters: str) -> bool:
    return ''.join(list(reversed(characters.replace(' ', '')))) == characters.replace(' ', '')


def is_palindrome_solution2(characters: str) -> bool:
    characters = characters.replace(' ', '')
    return True if len(characters) == sum([characters[i] == characters[-(i+1)]
                                           for i in range(len(characters))]) else False
