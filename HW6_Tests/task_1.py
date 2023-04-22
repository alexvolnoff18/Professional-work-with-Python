

# Дан список с визитами по городам и странам. Напишите код, который возвращает отфильтрованный список geo_logs, содержащий только визиты из России."


geo_logs_list = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]


def geo_logs_country(country_, geo_logs_list):
  """
  Функция возвращает отфильтрованный список geo_logs, содержащий только визиты
  в указанную страну (параметр country_)
  """
  filter_list = list(filter(lambda country: country_ in list(country.values())[0], geo_logs_list))
  return filter_list

print(geo_logs_country('Россия', geo_logs_list))