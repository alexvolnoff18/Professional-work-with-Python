

import datetime

# Задача №3 (Ссылка на старое ДЗ: https://github.com/alexvolnoff18/Opening-and-reading-a-file-writing-to-a-file/blob/main/main.py)

def logger(path):

    def __logger(old_function):
        def new_function(*args, **kwargs):
            date_time = datetime.datetime.now()
            arguments = f'{args}_{kwargs}'
            result = old_function(*args, **kwargs)
            with open(path, 'a', encoding='utf-8') as f:
                f.write(f'{date_time}, {old_function}, {arguments}, {result}')
            return result
        return new_function
    return __logger



path = 'cook_book.log'
@logger(path)
def my_cook_book(text_file):  # Функция из старого домашнего задания

    keys = ['ingridient_name', 'quantity', 'measure']
    with open(text_file, encoding='utf-8') as text:
        lines = filter(bool, map(str.strip, text))
        result = {n: [{k: v for (k, v) in zip(keys, map(str.strip, next(lines).split(' | ', 2)))}
                      for _ in range(int(next(lines)))] for n in lines}
    return result

my_cook_book("recipes.txt")
