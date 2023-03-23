

from pprint import pprint
import csv
import re
import openpyxl
import pandas as pd


PHONE_PATTERN = r'(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*'
PHONE_SUB = r'+7(\2)-\3-\4-\5 \6\7'


with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    # pprint(contacts_list)

  
# TODO 1: выполните пункты 1-3 ДЗ
def convert_list(contacts_list):
  '''
  Функция преобразует список в пронумированный словарь, помещает
  Фамилию, Имя и Отчество человека в поля lastname, firstname и 
  surname соответственно
  '''
  keys = (contacts_list[0])
  contacts_dict = [dict(zip(keys, values)) for values in contacts_list[1:]]
  num_contacts_dicts = {x: i for x, i in enumerate(contacts_dict, 1)}  
  for v in num_contacts_dicts.values():
      # print(len(v['lastname'].split()))
      if len(v['lastname'].split()) == 3:
        v['firstname'] = v['lastname'].split()[1]
        v['surname'] = v['lastname'].split()[2]
        v['lastname'] = v['lastname'].split()[0]
      elif len(v['lastname'].split()) == 2:
        v['firstname'] = v['lastname'].split()[1]
        v['lastname'] = v['lastname'].split()[0]
      elif len(v['firstname'].split()) == 2:
        v['surname'] = v['firstname'].split()[1]
        v['firstname'] = v['firstname'].split()[0]
  return num_contacts_dicts
  

def add_values(contacts_dicts):
  """
  Функция добавляет в словарь недостающие значения из 
  дублирующего словаря и удаляет дубликат
  """
  duplicate_position = []
  # добавляем в словарь недостающие значения
  for k, v in contacts_dicts.items():
    for count in range(len(contacts_dicts.keys())+1):
      if count != k and count > 0 and count > k and \
      contacts_dicts[k]['lastname'] == contacts_dicts[count]['lastname']:
        duplicate_position.append(count)
        for v in contacts_dicts[k]:
          if contacts_dicts[k][v] == contacts_dicts[count][v]:
            pass
          elif contacts_dicts[k][v] == '' and contacts_dicts[count][v] != '':
            contacts_dicts[k][v] = contacts_dicts[count][v]
   # удаляем дубликаты
  for i in duplicate_position:
    del contacts_dicts[i]


def phone_number_unification(contacts_dicts):
  """
  Функция приводит к единому стандарту (унифицирует)
  телефонные номера контактных лиц
  """
  for v in contacts_dicts.values():
    v['phone'] = re.sub(PHONE_PATTERN, PHONE_SUB, v['phone'])

    
def convert_dictionary_to_list(contacts_dicts):
  """
  Функция преобразует словарь в список
  """
  contact_list = []
  for v in contacts_dicts.values():
    for idx, sub in enumerate(contacts_dicts.values(), start = 0):
        if idx == 0:
            contact_list.append(list(sub.keys()))
            contact_list.append(list(sub.values()))
        else:
            contact_list.append(list(sub.values()))   
    return contact_list


if __name__ == '__main__':
  contacts_dicts = convert_list(contacts_list) #преобразуем список в словарь 
                                              #расставляем ФИО по местам  
  add_values(contacts_dicts) #Добавляем недостающие значения, удаляем дубликаты
  contacts_dicts = dict(enumerate(contacts_dicts.values(), 1))  #Обновляем нумерацию в словаре
  phone_number_unification(contacts_dicts) #приводитим к единому стандарту телефонные номера
  contact_list = convert_dictionary_to_list(contacts_dicts)#приобразую словарь в список


# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding='utf-8') as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(contact_list)


#Для более корректного вывода данных
df = pd.DataFrame(contacts_dicts) #Обработка и преобразование 
df = df.transpose()                #контактных данных в таблицу
print(df)
df.to_csv('table_phonebook.csv')  
df.to_excel('table_phonebook.xlsx')
  
 
