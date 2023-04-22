

# Напишите код для преобразования произвольного списка вида ['2018-01-01', 'yandex', 'cpc', 100] (он может быть любой длины) в словарь {'2018-01-01': {'yandex': {'cpc': 100}}}

list = ['2018-01-01', 'yandex', 'cpc', 100]



def list_in_dict(temp):
  """
  Функция преобразовывает произвольный список вида ['a', 'b', 'c', 0]
  в словарь вида {'a': {'b': {'c': 0}}} и возвращает его
  """
  if len(temp) == 2:
    x = {temp[0]: temp[1]}
    return x
  elif len(temp) > 2:
    x = {temp[0]: list_in_dict(temp[1:])}
    return x


print(list_in_dict(list))