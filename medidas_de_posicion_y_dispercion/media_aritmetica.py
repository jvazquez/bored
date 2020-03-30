import logging
import os
import sys

from typing import List, Tuple
from random import randint, randrange

from utils import Util


class ArithmeticMeanUtil(Util):
    def __init__(self):
        self.list_start_number = 1
        self.random_list_size = 10

    def random_list_generator(self, max_number: int, list_size: int) -> List:
        """
        Generate a pseudo random list that we use for averages

        :param max_number:
        :param list_size:
        :return:
        """

        output = []
        if max_number <= 0:
            max_number = 10

        if list_size <= 0:
            list_size = self.random_list_size

        for _ in range(1, list_size):
            output.append(randrange(self.list_start_number, max_number))

        return output


def problem_description():
    return """
    Se tomó una muestra de personas que fuman y se les preguntó por la edad que
    empezaron a adquirir ese hábito.
    Las respuesta fueron: 14, 16, 15, 18, 17, 19, 19, 18.
    """


class ArithmeticMean:
    @staticmethod
    def get_arithmetic_mean(problem_arguments: List) -> int:
        """
        Calculate the arithmetic mean of a list.
        :param problem_arguments:
        :return: int
        """
        return sum(problem_arguments) / len(problem_arguments)

    @staticmethod
    def property_one_description() -> str:
        return """Suma de las desviaciones entre cada valor observado 
        y su media aritmética es igual a cero, culaquiera sera la distribucion
        """

    @staticmethod
    def property_one(sample_values: List, mean_value: int) -> int:
        """
        La suma de las desviaciones entre cada valor observado y su media
        arimética es igual a 0.

        :param sample_values:
        :param mean_value:
        :return:
        """
        return int(sum(list(map(lambda x: x - mean_value, sample_values))))

    @staticmethod
    def property_two_description() -> str:
        return """La suma de los cuadrados de las desviaciones entre cada valor
        observado y su media aritmética es menor o igual que la suma de los
        cuadrados de desviaciones tomadas con respecto a cualquier otro valor.
        """

    @staticmethod
    def property_two(sample_values: List, mean_value: int) -> int:
        return int(sum(list(map(lambda x: (x - mean_value)**2, sample_values))))

    @staticmethod
    def property_three(random_element_one: int,
                       random_element_two: int,
                       operation: str = "add"
                       ) -> int:
        """
        If we've got two sets that have the same len, the sum or subtraction
        of two elements will be equal to the sum or subtraction of the mean
        of each individual elements.
        y_sub{i} = x1_sub{i} + x2_sub{i} == M(y) = M(x_sub{1}) + M(x_sub{2})
        @todo Spanish text is hard to understand... I'm not sure if they mean
        this.

        :param random_element_one:
        :param random_element_two:
        :param operation:
        :return: int
        """
        if operation == "add":
            individual_deviation_sum = random_element_one + random_element_two
            individual_mean_sum = (random_element_one / 1) +\
                                  (random_element_two / 1)
            operation_result = individual_deviation_sum == individual_mean_sum
        else:
            individual_deviation_subtratction = random_element_one -\
                                                random_element_two
            individual_mean_subtraction = (random_element_one / 1) - \
                                          (random_element_two / 1)
            operation_result = individual_deviation_subtratction == \
                individual_mean_subtraction

        return operation_result


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)

    age_sample = [14, 16, 15, 18, 17, 19, 19, 18]
    logging.info(problem_description())
    age_mean = ArithmeticMean.get_arithmetic_mean(age_sample)
    logging.info(ArithmeticMean.property_one_description())
    deviation_sum = ArithmeticMean.property_one(age_sample, age_mean)
    logging.info(deviation_sum)
    logging.info(ArithmeticMean.property_two_description())
    squared_deviation = ArithmeticMean.property_two(age_sample, age_mean)
    a_random_value = randint(1, 10)
    squared_deviation_with_random = ArithmeticMean.property_one(age_sample,
                                                                a_random_value)
    logging.info(f"{squared_deviation} <= {squared_deviation_with_random}."
                 f"Random is {a_random_value}")
    assert deviation_sum == 0
    amu = ArithmeticMeanUtil()
    sample_values_group_one = amu.random_list_generator(10, 8)
    sample_values_group_two = amu.random_list_generator(10, 8)
    random_index_picker = randrange(1, len(sample_values_group_one) - 1)
    logging.info(f"Random picked index {random_index_picker}")
    first_number = sample_values_group_one[random_index_picker]
    second_number = sample_values_group_two[random_index_picker]
    add_property_three = ArithmeticMean.property_three(first_number,
                                                       second_number,
                                                       "add"
                                                       )
    assert add_property_three is True
    subtraction_property_three = ArithmeticMean.property_three(first_number,
                                                               second_number
                                                               )
    assert subtraction_property_three is True
