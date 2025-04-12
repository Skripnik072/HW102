from time import time
from functools import wraps


def log(filename=''):
    ''' Декоратор для регистрации названия функции, её результатов и ошибок'''
    def my_decorators(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                start_time = time()
                result = func(*args, **kwargs)
                end_time = time()
                log_result = (f'{func.__name__} ok\n')
                if filename:
                    with open(filename, 'a', encoding='utf-8') as names_file:
                        names_file.write(log_result)
                elif not filename:
                    print(log_result)
                return result
            except Exception as e:
                log_result = (f' {func.__name__} error {e} Input: {args}, {kwargs}\n')
                if filename:
                    with open(filename, 'a', encoding='utf-8') as names_file:
                        names_file.write(log_result)
                else:
                    print(log_result)
            raise Exception(f"Ошибка в работе декоратора")

        return wrapper
    return my_decorators


@log()
def my_function(x, y):
    return x + y

my_function(3, 1)