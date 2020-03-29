import logging
import os

from itertools import permutations
from random import randint, seed
from typing import List


def permutations_n_c_r(a_random_list: List, groups_of_n_elements: int):
    """
    Per
    :param a_random_list:
    :param groups_of_n_elements:
    :return:
    """
    for i in permutations(a_random_list, groups_of_n_elements):
        print(f"<..{i}")
        yield i
        print("> back in generator")


if __name__ == '__main__':
    seed_number = os.getenv('SEED', 1)
    seed(seed_number)
    a_random_number = randint(2, 4)
    for x in permutations_n_c_r([1, 2, 3], a_random_number):
        print(f"|{x}|")
