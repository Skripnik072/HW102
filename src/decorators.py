from time import time

from typing import Callable

from typing import Any


def log(filename: str = "") -> str:
    """Декоратор для регистрации названия функции, её результатов и ошибок"""

    def my_decorators(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                start_time = time()
                result = func(*args, **kwargs)
                end_time = time()
                log_result = f"{func.__name__} ok Время работы: {round((end_time - start_time) * 1000000, 2)} c\n"
                if filename:
                    with open(filename, "a", encoding="utf-8") as names_file:
                        names_file.write(log_result)

                elif not filename:
                    print(log_result)
                return result
            except Exception as e:
                log_result = f" {func.__name__} error {e} Ошибка в работе декоратора. Input: {args}, {kwargs}\n"
                if filename:
                    with open(filename, "a", encoding="utf-8") as names_file:
                        names_file.write(log_result)
                else:
                    print(log_result)
            raise Exception("Ошибка в работе декоратора")

        return wrapper

    return my_decorators


@log()
def my_function(x: int, y: int) -> int:
    return x + y


my_function(3, 1)
