import unittest
from parameterized import parameterized
from HW6_Tests.task_3 import max_stats
from HW6_Tests.task_3 import stats


class TestSequence(unittest.TestCase):

    @parameterized.expand([
        ["truth", stats[max_stats(stats)], 120],
        ["false", stats[max_stats(stats)], 119],
    ])
    def test_numbers(self, name, a, b):
        """
        Функция тестирует на равенство максимального значения продаж
        """
        self.assertEqual(a, b)

    @parameterized.expand([
        ["truth", max_stats(stats), 'yandex'],
        ["false", max_stats(stats), 'vandex'],
    ])
    def test_strings(self, name, a, b):
        """
        Функция тестирует на соответствие названию рекламного канала
        с максимальным объемом продаж
        """
        self.assertMultiLineEqual(a, b)

    @parameterized.expand([
        ["truth", max_stats(stats), stats],
    ])
    def test_entry(self, name, a, b):
        """
        Функция тестирует на вхождение названия рекламного канала
        с максимальным объемом продаж в словарь со статистическими данными
        """
        self.assertIn(a, b)

if __name__ == '__main__':
  unittest.main()

