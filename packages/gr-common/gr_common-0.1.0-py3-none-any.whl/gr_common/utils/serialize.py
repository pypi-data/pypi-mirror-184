from functools import wraps
from typing import Any, Callable, TypeVar, get_type_hints

from pydantic import BaseModel, parse_obj_as

RT = TypeVar("RT")  # return type


def serialize(func: Callable[..., RT]) -> Callable[..., RT]:
    """
    Сериализация ответа функции, используя type hints
    """

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> RT:
        results = func(*args, **kwargs)

        if results:
            return_type = get_type_hints(func).get("return")
            if not return_type:
                raise ValueError("Установите возвращаемый тип функции")
            if not issubclass(return_type, BaseModel):
                raise TypeError("Возвращаемый тип должен быть наследован от pydantic.BaseModel")
            if isinstance(results, return_type):
                return results
            if isinstance(results, dict):
                return return_type(**results)
            return parse_obj_as(return_type, results)
        return results

    return wrapper
