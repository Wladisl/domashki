# Task 1. Напишіть функцію, що приймає один аргумент будь-якого типу та повертає цей аргумент, перетворений на float.
# Якщо перетворити не вдається функція має повернути 0.

def arg_to_float(arg):
    try:
        res = float(arg)
        return res
    except Exception:
        return 0


arg_input = input('Введіть значення: ')
result = arg_to_float(arg_input)
print(result)


# Task 2. Напишіть функцію, що приймає два аргументи. Функція повинна
# a. якщо аргументи відносяться до числових типів (int, float) - повернути перемножене значення цих аргументів,
# b.якщо обидва аргументи це строки (str) - обʼєднати в одну строку та повернути
# c. у будь-якому іншому випадку повернути кортеж з цих аргументів

def addition_function(arg1, arg2):
    if type(arg1) in (int, float) and type(arg2) in (int, float):
        return arg1 * arg2
    elif type(arg1) == type(arg2) == str:
        return arg1 + arg2
    else:
        return arg1, arg2


result1 = addition_function(23, 54353)
print(result1)

result2 = addition_function('Puzata ', "Xata")
print(result2)

result3 = addition_function(3, "323")
print(result3)


# Task 3. Перепишіть за допомогою функцій вашу программу "Касир в кінотеатрі", яка буде виконувати наступне:
# a. Попросіть користувача ввести свсвій вік.
# i- якщо користувачу менше 7 - вивести "Тобі ж <> <>! Де твої батьки?"
# ii- якщо користувачу менше 16 - вивести "Тобі лише <> <>, а це е фільм для дорослих!"
# iii- якщо користувачу більше 65 - вивести "Вам <> <>? Покажіть пенсійне посвідчення!"
# iv- якщо вік користувача містить 7 - вивести "Вам <> <>, вам пощастить"
# v- у будь-якому іншому випадку - вивести "Незважаючи на те, що вам <> <>, білетів всеодно нема!"
# b Замість <> <> в кожну відповідь підставте значення віку (цифру) та правильну форму слова рік.
# Для будь-якої відповіді форма слова "рік" має відповідати значенню віку користувача (1 - рік, 22 - роки, 35 - років і тд...).
# Наприклад :
# "Тобі ж 5 років! Де твої батьки?"
# "Вам 81 рік? Покажіть пенсійне посвідчення!"
# "Незважаючи на те, що вам 42 роки, білетів всеодно нема!"


def get_age():
    try:
        age = int(input('Введіть свій вік: '))
        return age
    except ValueError:
        print('Введене значення не є цілим числом')


def age_format(age):
    if age % 10 == 1 and age % 100 != 11:
        return f'{age} рік'
    elif 2 <= age % 10 <= 4 and age % 100 < 10:
        return f'{age} роки'
    else:
        return f'{age} років'


def program_cashier():
    age = get_age()

    if age is not None:
        if '7' in str(age):
            print(f'Вам {age_format(age)}, вам пощастить')
        elif age == 0:
            print(f'Вам {age_format(age)}, ви ще не народились')
        elif age < 7:
            print(f'Тобі ж {age_format(age)}! Де твої батьки?')
        elif age < 16:
            print(f'Тобі лише {age_format(age)}, а це фільм для дорослих!')
        elif age > 65:
            print(f'Вам {age_format(age)}? Покажіть пенсійне посвідчення!')
        else:
            print(f'Незважаючи на те, що вам {age_format(age)}, білетів всеодно нема!"')


program_cashier()
