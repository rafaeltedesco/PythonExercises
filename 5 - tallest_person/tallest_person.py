import random
from functools import reduce

from typing import Dict, List


def get_tallest_by_sex(sex: str, list_of_persons: List[Dict[str, float]]) -> Dict[str, float]:
    return reduce(lambda person, next_person: person if person['height'] > next_person['height'] else next_person, filter(
        lambda person: person['sex'] == sex, list_of_persons))


def get_average_height_by_sex(sex: str, list_of_persons: List[Dict[str, float]]) -> List[Dict[str, float]]:
    avg_height = round(
        reduce(
            lambda person, next_person: {
                'height': person['height'] + next_person['height']},
            filter(lambda person: person['sex'] == sex, list_of_persons), {'height': 0})['height'], 2)
    return {'avg_height': round(avg_height / len(list(filter(lambda person: person['sex'] == sex, list_of_persons))), 2)}


def generate_random_height(list_of_heights: List[float]):
    new_height = round(random.random() + 1, 2)
    if new_height in list_of_heights:
        generate_random_height(list_of_heights)
    return [*list_of_heights, new_height]
