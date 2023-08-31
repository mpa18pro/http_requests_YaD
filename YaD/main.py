import os
import requests


class YaUploader:
    def __init__(self, _token: str):
        self.token = _token

    def upload(self, file_path):
        """Метод загружает файл file_path на Яндекс.Диск"""
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        file_path.split('/', )[-1]
        headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(self.token)}
        params = {"path": f"{file_name}", "overwrite": "true"}
        get_upload_url = requests.get(upload_url, headers=headers, params=params)
        get_url = get_upload_url.json()
        href = get_url.get("href", "")
        responce = requests.api.put(href, data=open(file_path, 'rb'))
        responce.raise_for_status()
        if responce.status_code == 201:
            return 'Успешно'
        else:
            return f"Ошибка загрузки! Код ошибки: {responce.status_code}"


if __name__ == '__main__':
    # Здаем имя файла
    file_name = 'DSC_0971.JPG'
    # Задаем путь к файлу
    path_to_file = os.path.join(os.getcwd(), file_name)
    # Задаем токен
    token = ''
    uploader = YaUploader(token)
    print(f"Загружаем файл {path_to_file.split('/', )[-1]} на Яндекс.Диск")
    result = uploader.upload(path_to_file)
    print(result)
    print()