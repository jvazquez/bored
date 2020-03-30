import unittest

from media_aritmetica import ArithmeticMeanUtil


class TestArithmeticMeanUtil(unittest.TestCase):
    def test_random_list_generator_will_produce_a_list(self):
        arithmetic_mean_util = ArithmeticMeanUtil()
        output = arithmetic_mean_util.random_list_generator(20, 8)
        self.assertIs(list, type(output))

    def test_random_list_generator_will_not_have_negative_values(self):
        arithmetic_mean_util = ArithmeticMeanUtil()
        output = arithmetic_mean_util.random_list_generator(20, 8)
        self.assertNotIn(0, output)


if __name__ == '__main__':
    unittest.main()
