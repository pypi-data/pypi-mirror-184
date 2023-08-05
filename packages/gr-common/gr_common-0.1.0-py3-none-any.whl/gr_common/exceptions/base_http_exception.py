class BaseHTTPException(Exception):
    status: int
    message: str
