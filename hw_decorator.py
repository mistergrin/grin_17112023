import time


def decorator(func):
    def wrapper(*args):
        with open('txt.file.txt', mode='a', encoding='utf-8') as file:
            start_time_function = time.asctime()
            string = func(*args)
            end_time_function = time.asctime()
            file.write(f"function started at {start_time_function}, ended at {end_time_function}. Result - {string}\n")
    return wrapper


@decorator
def get_string(string):
    return string


@decorator
def get_another_string(another_string):
    return another_string


get_string("some_string")
get_another_string("another_string")
