from gr_common.exceptions.base_exception import BaseException


class ValueNotFoundException(BaseException):
    def __init__(self, key: str) -> None:
        self.message = f"Value for key: {key} not found"
