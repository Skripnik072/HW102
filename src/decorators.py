from time import time


def log(filename=""):
    """Декоратор для регистрации названия функции, её результатов и ошибок"""

    def my_decorators(func):
        def wrapper(*args, **kwargs):
            try:
                start_time = time()
                result = func(*args, **kwargs)
                end_time = time()
                log_result = f"{func.__name__} ok Time for work: {start_time - end_time}\n"
                if filename:
                    with open(filename, "a", encoding="utf-8") as names_file:
                        names_file.write(log_result)

                elif not filename:
                    print(log_result)
                return result
            except Exception as e:
                log_result = f" {func.__name__} error {e} Input: {args}, {kwargs}\n"
                if filename:
                    with open(filename, "a", encoding="utf-8") as names_file:
                        names_file.write(log_result)
                else:
                    print(log_result)
            raise Exception("Ошибка в работе декоратора")

        return wrapper

    return my_decorators


@log()
def my_function(x, y):
    return x + y


my_function(3, 1)
