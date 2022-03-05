from functools import reduce
from typing import Dict, List
import unittest
import random
from tallest_person import get_average_height_by_sex, get_tallest_by_sex


def generate_random_height(list_of_heights: List[float]):
    new_height = round(random.random() + 1, 2)
    if new_height in list_of_heights:
        generate_random_height(list_of_heights)
    return [*list_of_heights, new_height]


def get_persons_by_sex(sex: str, list_of_person: List[Dict[str, float]]):
    return filter(lambda person: person['sex'] == sex, list_of_person)


def sum_heights(person, next_person):
    return {'height': person['height'] + next_person['height']}


def get_tallest(person, next_person):
    return person if person['height'] > next_person['height'] else next_person


def get_mean_by_sex(total_height, sex, persons):
    return round(total_height / len(list(get_persons_by_sex(sex, persons))), 2)


class TestTallestPerson(unittest.TestCase):

    def setUp(self):
        self.heights = []
        while len(self.heights) != 10:
            self.heights = generate_random_height(self.heights)
        self.people = [
            ('Rafael', 'M'), ('Travis', 'M'),
            ('Larissa', 'F'), ('Giovanna', 'F'),
            ('Diogo', 'M'), ('Bianca', 'F'),
            ('Jorge', 'M'), ('Carlos', 'M'),
            ('Brenda', 'F'), ('Cleber', 'M')
        ]
        self.persons = [{'name': self.people[i][0],
                        'sex': self.people[i][1],
                         'height': self.heights[i]}
                        for i in range(len(self.heights))]

        self.tallest_man = reduce(
            get_tallest, get_persons_by_sex('M', self.persons))
        self.tallest_woman = reduce(
            get_tallest, get_persons_by_sex('F', self.persons))

        self.total_men = reduce(
            sum_heights, get_persons_by_sex('M', self.persons), {'height': 0})
        self.total_women = reduce(
            sum_heights, get_persons_by_sex('F', self.persons), {'height': 0})

        self.avg_men = get_mean_by_sex(
            self.total_men['height'], 'M', self.persons)

        self.avg_women = get_mean_by_sex(
            self.total_women['height'], 'F', self.persons)

    def test_get_tallest_by_sex(self):
        self.assertDictEqual(get_tallest_by_sex('M', self.persons), self.tallest_man,
                             f'The tallest man must be called {self.tallest_man["name"]}!')
        self.assertDictEqual(get_tallest_by_sex('F', self.persons), self.tallest_woman,
                             f'The tallest woman must be called {self.tallest_woman["name"]}!')

    def test_average_height_by_sex(self):
        self.assertDictEqual(
            get_average_height_by_sex('M', self.persons),
            {'avg_height': self.avg_men},
            f'Men average height should be {self.avg_men}')
        self.assertDictEqual(
            get_average_height_by_sex('F', self.persons),
            {'avg_height': self.avg_women},
            f'Women average height should be {self.avg_women}')


if __name__ == '__main__':
    unittest.main()
