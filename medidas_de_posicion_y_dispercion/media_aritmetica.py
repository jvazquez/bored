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
    def property_three(sample_values_group_one: List,
                       sample_values_group_two: List,
                       expected_index: int) -> Tuple:
        """
        If we've got two sets that have the same len, the sum or subtraction
        of two elements will be equal to the sum or subtraction of the mean
        of each individual elements.
        y_sub{i} = x1_sub{i} + x2_sub{i} == M(y) = M(x_sub{1}) + M(x_sub{2})
        @todo Spanish text is hard to understand... I'm not sure if they mean
        this.

        :param sample_values_group_one:
        :param sample_values_group_two:
        :param expected_index:
        :return: tuple
        """

        if len(sample_values_group_one) != len(sample_values_group_two):
            print("here 1")
            raise Exception("Sample values have different len")

        if len(sample_values_group_one) - 1 < expected_index or \
                expected_index > len(sample_values_group_one) - 1:
            print("here 2")
            raise Exception("Expected index is not in the right range for this"
                            "operation")
        try:
            # With list.index fails sometimes randomly
            sum_values = sample_values_group_one.index(expected_index) + \
                sample_values_group_two[expected_index]
            subtraction_values = sample_values_group_one.index(expected_index) - \
                sample_values_group_two[expected_index]

            mean_sum = int(sample_values_group_one.index(expected_index) / 1 +
                           sample_values_group_two.index(expected_index) / 1
                           )
            mean_subtraction = int(sample_values_group_one.index(expected_index)
                                   / 1 -
                                   sample_values_group_two.index(expected_index) /
                                   1
                                   )
            print(f"+ Individual elements: {sum_values} == {mean_sum},"
                  f"{subtraction_values} == {mean_subtraction}")
            return sum_values == mean_sum and subtraction_values ==\
                   mean_subtraction
        except ValueError:
            print(f"Wtf?. Expected index: {expected_index}\n"
                  f"SVGL1: {len(sample_values_group_one)}, {sample_values_group_one}"
                  f"SVGL2: {len(sample_values_group_two)}, {sample_values_group_two}"
                  )


if __name__ == '__main__':
    age_sample = [14, 16, 15, 18, 17, 19, 19, 18]
    print(problem_description())
    age_mean = ArithmeticMean.get_arithmetic_mean(age_sample)
    print(ArithmeticMean.property_one_description())
    deviation_sum = ArithmeticMean.property_one(age_sample, age_mean)
    print(deviation_sum)
    print(ArithmeticMean.property_two_description())
    squared_deviation = ArithmeticMean.property_two(age_sample, age_mean)
    a_random_value = randint(1, 10)
    squared_deviation_with_random = ArithmeticMean.property_one(age_sample,
                                                                a_random_value)
    print(f"{squared_deviation} <= {squared_deviation_with_random}."
          f"Random is {a_random_value}")
    assert deviation_sum == 0
    amu = ArithmeticMeanUtil()
    sample_values_group_one = amu.random_list_generator(10, 8)
    sample_values_group_two = amu.random_list_generator(10, 8)
    random_index_picker = randrange(1, len(sample_values_group_one) - 1)
    print(f"Random picked index {random_index_picker},"
          f"List len {len(sample_values_group_one)}")
    output = ArithmeticMean.property_three(sample_values_group_one,
                                           sample_values_group_two,
                                           random_index_picker)
    print(f"Output is {output}")
