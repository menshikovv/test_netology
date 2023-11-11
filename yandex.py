import requests
import unittest

class TestYandexDiskAPI(unittest.TestCase):
    def setUp(self):
        self.token = '1678b9eee1b1417caba45227a90f0777'
        self.base_url = 'https://cloud-api.yandex.net/v1/disk/resources'

    def test_create_folder_success(self):
        folder_name = 'test_folder'
        headers = {'Authorization': f'OAuth {self.token}'}

        response = requests.put(f'{self.base_url}?path={folder_name}', headers=headers)

        self.assertEqual(response.status_code, 201)

        response = requests.get(self.base_url, headers=headers)
        self.assertIn(folder_name, response.json()['_embedded']['items'])

        requests.delete(f'{self.base_url}?path={folder_name}', headers=headers)

    def test_create_folder_already_exists(self):
        folder_name = 'test_folder'
        headers = {'Authorization': f'OAuth {self.token}'}

        response = requests.put(f'{self.base_url}?path={folder_name}', headers=headers)

        response = requests.put(f'{self.base_url}?path={folder_name}', headers=headers)

        self.assertEqual(response.status_code, 409)

        requests.delete(f'{self.base_url}?path={folder_name}', headers=headers)

    def test_create_folder_invalid_token(self):
        folder_name = 'test_folder'
        invalid_token = 'INVALID_TOKEN'
        headers = {'Authorization': f'OAuth {invalid_token}'}

        response = requests.put(f'{self.base_url}?path={folder_name}', headers=headers)

        self.assertEqual(response.status_code, 401)

if __name__ == '__main__':
    unittest.main()