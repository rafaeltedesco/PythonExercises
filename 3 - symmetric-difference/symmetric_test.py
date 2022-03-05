from symmetric import get_symmetric


class TestSymmetricDifference:

    def test_is_symmetric(self):
        assert get_symmetric([1, 2, 3], [5, 2, 1, 4]) == [3, 4, 5]

    def test_should_return_only_three_elements(self):
        assert len(get_symmetric([1, 2, 3], [5, 2, 1, 4])) == 3

    def test_should_not_contains_duplicateds_in_the_same_list(self):
        assert get_symmetric([1, 2, 3, 3], [5, 2, 1, 4]) == [3, 4, 5]
