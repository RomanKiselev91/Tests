from unittest import TestCase, main
import requests


access_token = 'y0__xC08su4BhjblgMg0cj24BJE4l5nQiqWXb8TVb-ViZH8oMP5Aw'
headers = {"Authorization": f"OAuth {access_token}"}
URL = "https://cloud-api.yandex.net/v1/disk/resources"

def create_folder(path):
    requests.put(f'{URL}?path={path}', headers=headers)
    return path

def meta_inf(path):
    resp = requests.get(f'{URL}?path={path}', headers=headers)
    resp.raise_for_status()
    return resp.json()
metainf = meta_inf(create_folder('Folder_test'))


class CreateFolder(TestCase):
    def test_create_folder(self):
        self.assertEqual(create_folder('Folder_test'), metainf['name'])


if __name__== '__main__':
    main()