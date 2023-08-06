import webbrowser

from gdshoplib.core.settings import VKSettings


class VK:
    def __init__(self):
        self.settings = VKSettings()

    def get_access_token(self):
        # Получить токен для работы
        # Открыть браузер для авторизации
        # Запустить веб сервер
        # Принять код, получить access_token и напечатать его
        # Убить сервер
        webbrowser.get("google-chrome").open("elearning.wsldp.com/python3/")

    def _get_code_url(self):
        return f"{self.settings.AUTH_URL}?\
            client_id=1\
            &display=page\
            &redirect_uri=http://example.com/callback\
            &group_ids=123456,654321\
            &scope=messages\
            &response_type=code\
            &v=5.131"

    @staticmethod
    def _start_code_reciver():
        ...
