import unittest
from parameterized import parameterized
from HW6_Tests.task_1 import geo_logs_country
from HW6_Tests.task_1 import geo_logs_list

class TestSequence(unittest.TestCase):

    @parameterized.expand([
        ["truth_1", geo_logs_country('Россия', geo_logs_list),
         [{'visit1': ['Москва', 'Россия']}, {'visit3': ['Владимир', 'Россия']}, {'visit7': ['Тула', 'Россия']},
          {'visit8': ['Тула', 'Россия']}, {'visit9': ['Курск', 'Россия']}, {'visit10': ['Архангельск', 'Россия']}]],
        ["false", geo_logs_country('Россия', geo_logs_list), [{'visit2': ['Дели', 'Индия']}]],
        ["truth_2", geo_logs_country('Индия', geo_logs_list), [{'visit2': ['Дели', 'Индия']}]]
    ])
    def test_lists(self, name, a, b):
        """
        Функция тестирует на соответствие полученного списка искомому
        """
        self.assertListEqual(a, b)

    @parameterized.expand([
        ["truth_1", geo_logs_country('Россия', geo_logs_list)[1], geo_logs_list],
        ["truth_2", geo_logs_country('Индия', geo_logs_list)[0], geo_logs_list],
    ])
    def test_entry(self, name, a, b):
        """
        Функция тестирует на вхождение полученног списка в исходный список geo_logs
        """
        self.assertIn(a, b)

    @parameterized.expand([
        ["truth_1", geo_logs_country('Афганистан', geo_logs_list)],
        ["truth_2", geo_logs_country('Зимбабве', geo_logs_list)],
        ["false", geo_logs_country('Россия', geo_logs_list)]
    ])
    def test_falsehood(self, name, a):
        """
        Функция тестирует на вывод данных при поиске несуществующих в исходном
        списке geo_logs стран
        """
        self.assertFalse(a)

if __name__ == '__main__':
  unittest.main()