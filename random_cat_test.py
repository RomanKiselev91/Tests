
'''Напиши автотест на Яндекс.диск
1. Создание папки
2. Загрузка туда файла по ссылке(https://cataas.com/) любого кота
3. Проверить что файл загрузился
4. Работаем через апи.
5. Всё это залить на гитхаб.'''

from unittest import TestCase, main
import requests


access_token = ''
headers = {"Authorization": f"OAuth {access_token}"}
URL = "https://cloud-api.yandex.net/v1/disk/resources"
URL_image = 'https://cataas.com/cat/says/'
DISK_API_URL = 'https://cloud-api.yandex.net/v1/disk'

URL_UPLOAD = 'https://cloud-api.yandex.net/v1/disk/resources/upload?'

def create_folder(path):
    requests.put(f'{URL}?path={path}', headers=headers)
    return path

folder = create_folder('CAT')

def save_disk():
    response = requests.post(URL_UPLOAD, headers=headers,
                                params={'path': f'{folder}/{'CAT'+'.jpg'}', 'url': f'{URL_image + 'CAT'}'})
    return response
save_disk()


def meta_inf(path):
    resp = requests.get(f'{URL}?path={path}', headers=headers)
    resp.raise_for_status()
    return resp.json()
metainf = meta_inf(folder)


class TestCreateFolder(TestCase):
    def test_create_folder(self):
        self.assertEqual(folder, metainf['name'])

class TestCheckFile(TestCase):
    def check_file(self):
        check = requests.get(f'{DISK_API_URL}/resources', headers=headers, params={'path': f'{'disk:/CAT'}/CAT.jpg'})
        self.assertEqual(check.status_code, 200)

if __name__== '__main__':
    main()



