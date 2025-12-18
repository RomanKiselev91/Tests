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


def save_disk():
    response = requests.post(URL_UPLOAD, headers=headers,
                                params={'path': f'{create_folder('CAT')}/{'CAT'+'.jpg'}', 'url': f'{URL_image + 'CAT'}'})
    return response



def meta_inf(path):
    resp = requests.get(f'{URL}?path={path}', headers=headers)
    resp.raise_for_status()
    return resp.json()



class TestCreateFolder(TestCase):
    def test_create_folder(self):
        self.assertEqual(create_folder('CAT'), meta_inf(create_folder('CAT'))['name'])

class TestCheckFile(TestCase):
    def check_file(self):
        check = requests.get(f'{DISK_API_URL}/resources', headers=headers, params={'path': f'{'disk:/CAT'}/CAT.jpg'})
        self.assertEqual(check.status_code, 200)

if __name__== '__main__':
    main()
