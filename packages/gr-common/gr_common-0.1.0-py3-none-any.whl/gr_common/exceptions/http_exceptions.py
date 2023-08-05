from gr_common.exceptions.base_http_exception import BaseHTTPException


class NotFoundHTTPException(BaseHTTPException):
    status: int = 404
    message: str = "Object does not exist"

    def __init__(self, message: str | None = None) -> None:
        if message:
            self.message = message
