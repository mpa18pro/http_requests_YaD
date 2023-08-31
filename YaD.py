import os
import requests


class YaUploader:
    def __init__(self, _token: str):
        self.token = _token

    def upload(self, file_path):
        """Метод загружает файл file_path на Яндекс.Диск"""
        # Определяем запрос для получения ссылки согласно документации Yandex.API
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        # Выделяем имя загружаемого файла
        file_path.split('/', )[-1]
        # Определяем формат заголовков запроса
        headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(self.token)}
        # Определяем параметры запроса (назначаем путь загрузки, имя файла и разрешаем перезапись)
        params = {"path": f"{file_name}", "overwrite": "true"}
        # Выполняем запрос на получение ссылки для загрузки
        get_upload_url = requests.get(upload_url, headers=headers, params=params)
        get_url = get_upload_url.json()
        # Выделяем ссылку для загрузки в отдельную переменную
        href = get_url.get("href", "")
        # Выполняем запрос на загрузку файла на Яндекс.Диск по полученной ссылке
        responce = requests.api.put(href, data=open(file_path, 'rb'))
        # Получаем статус отправки файла
        responce.raise_for_status()
        # Проверяем успешность отправки по полученному статусу
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
    # Определяем экземпляр класса для токена пользователя
    uploader = YaUploader(token)
    # Загружаем файл на диск
    print(f"Загружаем файл {path_to_file.split('/', )[-1]} на Яндекс.Диск")
    result = uploader.upload(path_to_file)
    print(result)
    print()