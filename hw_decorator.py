import time


def decorator(func):
    def wrapper(*args):
        with open('txt.file.txt', mode='a', encoding='utf-8') as file:
            start_time_function = time.asctime()
            result = func(*args)
            end_time_function = time.asctime()
            file.write(f"function started at {start_time_function}, ended at {end_time_function}. Result - {result}\n")
            return result
    return wrapper


@decorator
def get_string(string):
    return string


@decorator
def get_number(number):
    return number * 3


get_string("some_string")
get_number(34849932)
