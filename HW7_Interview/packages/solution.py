
class Stack(list):
    """Реализую класс Stack со следующими методами:
    is_empty — проверка стека на пустоту. Метод возвращает True или False;
    push — добавляет новый элемент на вершину стека. Метод ничего не возвращает;
    pop — удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека;
    peek — возвращает верхний элемент стека, но не удаляет его. Стек не меняется;
    size — возвращает количество элементов в стеке.
    """

    def is_empty(self):
        return len(self) == 0

    def push(self, item):
        self.append(item)

    def pop(self):
        if not self.is_empty():
            item = self[-1]
            self.__delitem__(-1)
        return item

    def peek(self):
        if not self.is_empty():
            return self.__getitem__(-1)

    def size(self):
        return len(self)


def check_brackets(list):
    stack = Stack()
    brackets_dict = {'(': ')', '[': ']', '{': '}'}
    for elem in list:
        for item in elem:
            if item in brackets_dict:
                stack.push(item)
            elif item == brackets_dict.get(stack.peek()):
                stack.pop()
            else:
                return False
        return stack.is_empty()


def balance_information(old_function):
    """
    Декоратор. Выводит информацию о сбаланнсированности/несбаланнсированности списка
    передаваемого в функцию 'check_brackets()'
    """
    if old_function is False:
        print("Несбалансированно")
    else:
        print("Сбалансированно")