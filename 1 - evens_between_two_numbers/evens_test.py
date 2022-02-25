import evens_ex2
import evens


class TestEvensEx2:

    def test_evens_ex2_is_even(self):
        assert evens_ex2.get_evens(10, 20) == [12, 14, 16, 18]

    def test_evens_ex2_reversed_numbers(self):
        assert evens_ex2.get_evens(8,  2) == [4, 6]

    def test_evens_ex2_equal_numbers(self):
        assert evens_ex2.get_evens(2, 2) == []


class TestEvensEx1:
    def test_evens_ex1_is_even(self):
        assert evens.get_even_numbers(
            10, 20) == {'evens': [12, 14, 16, 18], 'count': 4}

    def test_evens_ex1_reversed_numbers(self):
        assert evens.get_even_numbers(8,  2) == {'evens': [4, 6], 'count': 2}

    def test_evens_ex1_equal_numbers(self):
        assert evens.get_even_numbers(2, 2) == {'evens': [], 'count': 0}
