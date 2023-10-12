# Task. Наришіть декоратор, який вимірює час виконання функції
# Задекоруйте цим декоратором вашу програму "Касир"

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


@time_teller_decorator
def program_cashier():
    age = get_number()

    if age is not None:
        age_format = answer_ending(age)
        if '7' in str(age):
            print(f'Вам {age_format}, вам пощастить')
        elif age == 0:
            print(f'Вам {age_format}, ви ще не народились')
        elif age < 7:
            print(f'Тобі ж {age_format}! Де твої батьки?')
        elif age < 16:
            print(f'Тобі лише {age_format}, а це фільм для дорослих!')
        elif age > 65:
            print(f'Вам {age_format}? Покажіть пенсійне посвідчення!')
        else:
            print(f'Незважаючи на те, що вам {age_format}, білетів всеодно нема!"')


program_cashier()
