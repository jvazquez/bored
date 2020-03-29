from typing import List
from random import randint


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
