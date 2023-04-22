import requests
import pytest
import time
from HW6_Tests.task_ya_api import DownloaderYandex
import token_ya


object = DownloaderYandex(token_ya.token_yandex())
name_folders = list(time.gmtime()[0:3])[::-1]
name_folders = '.'.join(list(map(str, name_folders))) + '_new'

@pytest.mark.parametrize('queries', [name_folders + '_1', name_folders + '_2'])
def test_delete_folder(queries):
    with pytest.raises(AssertionError):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        responder = requests.delete(url, headers=object.headers_yandex, params={'path': queries})
        assert '<Response [204]>' in str(responder)

@pytest.mark.parametrize('queries', ['new_1', 'new_2'])
def test_create_folder(queries):
    result = object.create_folder(queries)
    assert '<Response [201]>' in str(result[1]), f'Папка не создана: {result[1]}'
    assert type(result[0]) == str, f'Имя папки не строка: {type(result[0])}'
    assert 'new' in result[0], f'Слова new не входит в название папки: {result[0]}'
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    responder = requests.get(url, headers=object.headers_yandex, params={'path': result[0]}).json()
    assert 'disk' in responder['path'] , f'Папка в наличии: {responder["path"]}'

@pytest.mark.parametrize('queries', ['new_1', 'new_2'])
def test_checking_folders(queries):
    result = object.create_folder(queries)
    assert '<Response [409]>' in str(result[1]), f'Папка уже существует: {result[1]}'

@pytest.mark.skip(reason='просто пропускаем')
@pytest.mark.parametrize('queries', ['new_1', 'new_2'])
def test_checking_folders(queries):
    result = object.create_folder(queries)
    assert '<Response [401]>' in str(result[1])

@pytest.mark.parametrize('queries', [name_folders + '_1', name_folders + '_2'])
def test_delete_folders(queries):
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    responder = requests.delete(url, headers=object.headers_yandex, params={'path': queries})
    assert '<Response [204]>' in str(responder), f'Папка отсутствует: {responder}'


if __name__ == '__main__':
    pytest.main()  
