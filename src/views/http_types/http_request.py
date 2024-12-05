class HttpRequest:
    def __init__(self, body: dict = None, headers: dict = None):
        self.headers = headers
        self.body = body