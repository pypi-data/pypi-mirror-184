from abc import ABC, abstractmethod
from typing import Any, TypeAlias
from uuid import UUID

Key: TypeAlias = str | int | UUID
Data: TypeAlias = dict | str


class NoSqlInterface(ABC):
    @abstractmethod
    def put(self, key: Key, data: Data, *args: Any, **kwargs: Any) -> None:
        ...

    @abstractmethod
    def get(self, key: Key, *args: Any, **kwargs: Any) -> Data:
        ...

    @abstractmethod
    def remove(self, key: Key, *args: Any, **kwargs: Any) -> None:
        ...

    @abstractmethod
    def get_many(self, *args: Any, **kwargs: Any) -> list | dict | tuple:
        ...
