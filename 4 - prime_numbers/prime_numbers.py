

from typing import List


def is_prime_number(number: int):
  """
    Função deve verificar se número é primo ou não
    Deve retornar True se primo e False se não primo
    
    Lembrete: Um número é primo se ele for divísivel por 1 e por ele mesmo apenas
  """
  count = 0
  for i in range(1, number + 1):
    if count > 2:
      return False
    if number % i == 0:
      count += 1
  return True if count == 2 else False