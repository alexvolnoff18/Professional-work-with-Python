import unittest
from parameterized import parameterized
from HW7_Interview.packages.solution import Stack

class TestSequence(unittest.TestCase):

    @parameterized.expand([
        [Stack([1, 2, 22]).is_empty(), "Test OK!"],
        [Stack([43]).is_empty(), "Test OK!"],
    ])
    def test_is_empty_false(self, boolean_value, msg):
        """
        Тест метода 'is_empty()' класса 'Stack' на выполнение условия 'False'
        Если список не пуст, метод должен возвращать 'False'
        """
        self.assertFalse(boolean_value, msg)


    @parameterized.expand([
          [Stack([]).is_empty(), "Test OK!"]
      ])
    def test_is_empty_true(self, boolean_value, msg):
        """
        Тест метода 'is_empty()' класса 'Stack' на выполнение условия 'True'
        Если список пуст, метод должен возвращать 'True'
        """
        self.assertTrue(boolean_value, msg)


    def test_list_equality(self):
        """
        Тест метода 'push()' класса 'Stack' на выполнение своего функционала
        Проверяется равенство контрольного стека 'check_list' с полученным после
        применения метода 'push()' стеком 'processed_list'
        """
        initial_list = [1, 2, 3, 4]
        processed_list = Stack(initial_list)
        processed_list.push(99)
        processed_list.push(105)
        check_list = [1, 2, 3, 4, 99, 105]
        self.assertEqual(processed_list, check_list)


    @parameterized.expand([
        [Stack([1, 2, 3, 56]).pop(), 56, "Test OK!"],
        [Stack([600, 205, 999]).pop(), 999, "Test OK!"],
        [Stack([600, 205, 999]).pop(), 555, "Test failed!"],
    ])

    def test_pop_item_equality(self, pop_item, check_item, msg):
        """
        Тест метода 'pop()' класса 'Stack' на выполнение своего функционала
        Проверяется равенство удаленного элемента стека 'pop_item' с контрольным
        элементом 'check_item'
        """
        self.assertEqual(pop_item, check_item, msg)


    def test_pop_del_item(self):
        """
        Тест метода 'pop()' класса 'Stack' на выполнение своего функционала
        Проверяется на неравенство контрольного стека 'check_list' со стеком
        'processed_list' после применения метода 'pop()', т.к. метод должен удалять
        элементы из стека, они не должны быть равны
        """
        initial_list = [1, 2, 3, 4, 99, 105]
        processed_list = Stack(initial_list)
        processed_list.pop()
        check_list = [1, 2, 3, 4, 99, 105]
        self.assertNotEqual(processed_list, check_list)


    @parameterized.expand([
        [Stack([1, 2, 3, 56]).peek(), 56, "Test OK!"],
        [Stack([600, 205, 999]).peek(), 999, "Test OK!"],
        [Stack([600, 205, 999]).peek(), Stack([600, 205, 999]).pop(), "Test OK!"],
        [Stack([600, 205, 85]).peek(), 77, "Test failed!"],
    ])

    def test_peek(self, peek_item, check_item, msg):
        """
        Тест метода 'peek()' класса 'Stack' на выполнение своего функционала
        Проверяется равенство верхнего элемент стека с контрольным элементом
        'check_item'
        """
        self.assertEqual(peek_item, check_item, msg)


    def test_peek_not_del_item(self):
        """
        Тест метода 'peek()' класса 'Stack' на выполнение своего функционала
        Проверяется равенство контрольного стека 'check_list' со стеком 'processed_list'
        после применения метода 'peek()', т.к. метод не должен
        удалять элементы из стека, они должны быть равны
        """
        initial_list = [1, 2, 3, 4, 99, 105]
        processed_list = Stack(initial_list)
        processed_list.peek()
        check_list = [1, 2, 3, 4, 99, 105]
        self.assertEqual(processed_list, check_list)


    @parameterized.expand([
        [Stack([1, 2, 3, 56]).size(), len([1, 2, 3, 56]), "Test OK!"],
        [Stack([600, 205, 999]).size(), len([600, 205, 999]), "Test OK!"],
        [Stack([600, 205, 999]).size(), 3, "Test OK!"],
        [Stack([600, 205, 999, 669, 89]).size(), 10, "Test failed!"],
    ])

    def test_size_equality(self, method_size, check_size, msg):
        """
        Тест метода 'size()' класса 'Stack' на выполнение своего функционала
        Проверяется равенство длины стека 'method_size', определенной методом 'size()',
        с контрольной длиной 'check_size'
        """
        self.assertEqual(method_size, check_size, msg)


if __name__ == '__main__':
  unittest.main()