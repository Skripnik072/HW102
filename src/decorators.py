from time import time
from functools import wraps


def log(filename):
    '''Декоратор для вывода результатов в файл или в консоль'''
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                log_result = (f'{func.__name__} "ok" "Result" {result}\n')
                if filename:
                    with open(filename, 'a', encoding='utf-8') as names_file:
                        names_file.write(log_result)
                        print(log_result)
                        return result
            except Exception as e:
                log_result = (f'{func.__name__} "error" {e} "Input:" {args}, {kwargs}')
                if filename:
                    with open(filename, 'a', encoding='utf-8') as names_file:
                        names_file.write(log_result)
                        print(log_result)
            raise Exception(f"Max retries exceeded")

        return wrapper
    return decorator


def my_decorators(func):
    ''' Декоратор для регистрации названия функции, её результатов и ошибок'''
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        return result
    return wrapper


#def log(filename):
#    ''' Декоратор для регистрации названия функции, её результатов и ошибок'''
#    def my_decorators(func):
#        def wrapper(*args, **kwargs):
#            start_time = time()
#            result = func(*args, **kwargs)
#            end_time = time()

#            if result <= 0:
#                log_result = (f' {func.__name__} "error" "Input:" {args}, {kwargs} "Result:" {result}')
#                if filename:
#                    with open(filename, 'w', encoding='utf-8') as names_file:
#                        names_file.write(log_result)
#                print(log_result)
#                raise ValueError(log_result)
#            log_result = (f'{func.__name__} "ok" "Result" {result}')

#            if filename:
#                with open(filename, 'w', encoding='utf-8') as names_file:
#                    names_file.write(log_result)
#            print(log_result)

#            return result
#        return wrapper
#    return my_decorators


@log(filename="mylog.txt")
@my_decorators
def my_function(x, y):
    return x + y

my_function(3, 1)

