

import requests
import csv
from bs4 import BeautifulSoup
from fake_headers import Headers
import json

# стандартная страница для парсинга
base_url = 'https://spb.hh.ru/search/vacancy?text=python&area=1&area=2'
# Список для записи данных из подходящих вакансий
vacancy_list = []


def get_headers():
    """
    Данная функция задает заголовки.
    """
    return Headers(browser="firefox", os="win").generate()


def data_sampling(vacancies):
    """
    Данная функция собирает и записывает в список 'vacancy_list' данные из подходящих условиям вакансия - ссылка, вилка зп, название компании, город
    Условия задаются в 'if '...' in description_vacancy or '...' in description_vacancy:'
    """
    for vacancy in vacancies:
        description_vacancy = str(vacancy.find("div", class_="g-user-content")).lower()
        if 'django' in description_vacancy or 'sql' in description_vacancy:
            vacancy_link = vacancy.find("a", class_="serp-item__title")["href"]
            vacancy_company = vacancy.find('a', class_='bloko-link bloko-link_kind-tertiary').text
            vacancy_city = vacancy.find("div", {"data-qa": "vacancy-serp__vacancy-address"}).text.split(",")[0]
            if vacancy.find("span", {"data-qa": "vacancy-serp__vacancy-compensation"}) is None:
                vacancy_salary = "Зарплата не указана!"
            else:
                vacancy_salary = vacancy.find("span", {"data-qa": "vacancy-serp__vacancy-compensation"}).text
            vacancy = [
                f"Ссылка на вакансию: {vacancy_link}, Компания: {vacancy_company}, Город: {vacancy_city}, Зарплата: {vacancy_salary}"]
            vacancy_list.append(vacancy)


if __name__ == '__main__':
    html = requests.get(base_url, headers=get_headers()).text
    soup = BeautifulSoup(html, features="html5lib")
    vacancies = soup.find_all("div", class_="vacancy-serp-item__layout")
    data_sampling(vacancies)
    num_vacancy_dicts = {x: i for x, i in enumerate(vacancy_list, 1)}
    print(num_vacancy_dicts)  # Вывожу получившийся словарь, чтобы проверить, что подходящие вакансии нашлись.

    # Записываю данные в json
    with open('data_file.json', 'w') as f:
        json.dump(num_vacancy_dicts, f, sort_keys=True, indent=2)
    # Записываю данные в csv
    with open("data_file.csv", "w", encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(vacancy_list)