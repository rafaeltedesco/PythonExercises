from palindrome_ex1 import is_palindrome_solution1, is_palindrome_solution2


class TestPalindromeSolution1:

    def test_is_palindrome(self):
        assert is_palindrome_solution1('radar') == True
        assert is_palindrome_solution1('a grama é amarga') == True

    def test_is_not_palindrome(self):
        assert is_palindrome_solution1('fogo') == False
        assert is_palindrome_solution1('passeio no parque') == False


class TestPalindromeSolution2:

    def test_is_palindrome(self):
        assert is_palindrome_solution2('radar') == True
        assert is_palindrome_solution2('a grama é amarga') == True

    def test_is_not_palindrome(self):
        assert is_palindrome_solution2('fogo') == False
        assert is_palindrome_solution2('passeio no parque') == False
