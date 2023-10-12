import time


def time_teller_decorator(func):
    def _wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        difference_in_time = end - start
        print(f'Час виконання програми {difference_in_time}')
        return res

    return _wrapper


def get_number():
    try:
        age = int(input('Введіть свій вік: '))
        return age
    except ValueError:
        print('Введене значення не є цілим числом')


def answer_ending(age):
    if age % 10 == 1 and age % 100 != 11:
        return f'{age} рік'
    elif 2 <= age % 10 <= 4 and (age % 100 < 10 or age % 100 >= 20):
        return f'{age} роки'
    else:
        return f'{age} років'
