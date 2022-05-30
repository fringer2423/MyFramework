# Обработка GET-запроса с параметрами
class GetRequests:

    @staticmethod
    def parse_input_data(data: str):
        result = {}
        if data:
            # Делим параметры через &
            params = data.split('&')
            for item in params:
                # Делим ключ и значение через =
                k, v = item.split('=')
                result[k] = v
        return result

    @staticmethod
    def get_request_params(environ):
        # Получаем параметры запроса
        query_string = environ['QUERY_STRING']
        # Превращаем параметры в словарь
        request_params = GetRequests.parse_input_data(query_string)
        return request_params


# Обработка POST-запроса с параметрами
class PostRequests:

    @staticmethod
    def parse_input_data(data: str):
        result = {}
        if data:
            # Делим параметры через &
            params = data.split('&')
            for item in params:
                # Делим ключ и значение через =
                k, v = item.split('=')
                result[k] = v
        return result

    @staticmethod
    def get_wsgi_input_data(env) -> bytes:
        # Получаем длину тела
        content_length_data = env.get('CONTENT_LENGTH')
        # Приводим к int
        content_length = int(content_length_data) if content_length_data else 0
        # Считываем данные, если они есть
        data = env['wsgi.input'].read(content_length) if content_length > 0 else b''
        return data

    def parse_wsgi_input_data(self, data: bytes) -> dict:
        result = {}
        if data:
            # Декодируем данные
            data_str = data.decode(encoding='utf-8')
            # Собираем их в словарь
            result = self.parse_input_data(data_str)
        return result

    def get_request_params(self, environ):
        # Получаем данные
        data = self.get_wsgi_input_data(environ)
        # Превращаем данные в словарь
        data = self.parse_wsgi_input_data(data)
        return data
