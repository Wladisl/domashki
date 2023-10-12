# Task. Створіть файл lib.py, помістіть в нього допоміжні функції вашої програми "Касир".
# Імпортуйте їх для основної функції в основний файл. Запустіть "Касир" з основного файлу
# Помістіть в lib.py декоратор для вимірювання часу. Імпортуйте декоратор в основний файл, задекоруйте основну функцію "Касир".

from lib import time_teller_decorator
from lib import get_number
from lib import answer_ending


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
