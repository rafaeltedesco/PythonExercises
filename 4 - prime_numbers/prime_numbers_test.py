from operator import is_
import unittest
from prime_numbers import is_prime_number

class TestPrimeNumbers(unittest.TestCase):

  def setUp(self):
    self.primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    self.not_primes = [n for n in range(1, 100) if n not in self.primes]

  def test_is_prime(self):
    for number in self.primes:
      self.assertEqual(is_prime_number(number), True, f'O número {number} deve retornar True!')

  def test_is_not_prime(self):
    for number in self.not_primes:
      self.assertNotEqual(is_prime_number(number), True, f'O número {number} deve retornar False!')
    


if __name__ == '__main__':
  unittest.main()
  