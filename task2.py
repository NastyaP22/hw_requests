import requests

token = 'y0_AgAAAABQ2RFCAADLWwAAAADjKbu02uw28PIPQDWyjJzGijYoLF9ZKUA'

class YandexUpload:
    def __init__(self, token):
        self.token = token
    
    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def upload(self, file_path, file_name):
        self.file_path = file_path
        self.file_name = file_name
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': file_path, 'overwrite': 'true'}
        response = requests.get(url=url, headers=headers, params=params)
        response_data = response.json()
        href = response_data['href']
        response = requests.put(href, data=open(file_name, 'rb'))
        if response.status_code == 201:
            return 'success'

yandextest = YandexUpload('y0_AgAAAABQ2RFCAADLWwAAAADjKbu02uw28PIPQDWyjJzGijYoLF9ZKUA')
print(yandextest.upload('f1.txt', 'f1.txt'))