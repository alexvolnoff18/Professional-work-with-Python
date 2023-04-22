import unittest
from parameterized import parameterized
from HW6_Tests.task_2 import list_in_dict
from HW6_Tests.task_2 import list


class TestSequence(unittest.TestCase):

  @parameterized.expand([
        ["truth", list_in_dict(list), {'2018-01-01': {'yandex': {'cpc': 100}}}],
        ["false_1", list_in_dict(list), {'2018-01-01': {'yandex': {'cpc': 101}}}],
        ["false_2", list_in_dict(list), {'2018-01-01': 'yandex', 'cpc': 100}],
        ["truth_2", list_in_dict(list), {'2018-01-01': {'yandex': {'cpc': 100}}}]
    ])
  def test_dicts(self, name, a, b):
    """
    Функция тестирует на соответствие полученного словаря словарю,
    который необходимо получить по условию задачи
    """
    self.assertDictEqual(a, b)
#
#
if __name__ == '__main__':
  unittest.main()