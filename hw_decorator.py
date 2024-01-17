from datetime import datetime


def decorator(func):
    def wrapper(*args):
        with open('txt.file.txt', mode='a', encoding='utf-8') as file:
            string = func(*args)
            time = datetime.now()
            file.write(f"{string}; time - {time}\n")
    return wrapper


@decorator
def get_string(string):
    return string


@decorator
def get_another_string(another_string):
    return another_string


get_string("some_string")
get_another_string("another_string")
