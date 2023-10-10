# Task Доопрацюйте гру з занятя наступним чином:
#
# додайте підказки для користувача.
# якщо різниця між числами 1-2 - "Гаряче"
# якщо різниця між числами 3-5 - "Тепло"
# якщо різниця між числами 6 і більше- "Холодно"
# додайте лічильник спроб вгадати.
# користувач повинен вгадати число за фіксовану кількість спроб (визначіть кількість спроб самостійно).
# якщо він не вгадав за фіксовану кількість спроб - гра завершується з відповідним повідомленням


from random import randint


def get_user_number(prompt='Enter number', lower_limit=None, upper_limit=None):
    while True:
        try:
            res = int(input(f'{prompt} (int number): '))
        except Exception:
            print('Wrong input!')
        else:
            if lower_limit is not None:
                if res < lower_limit:
                    print(f'Number should be bigger than {lower_limit}!')
                    continue
            if upper_limit is not None:
                if res > upper_limit:
                    print(f'Number should be less than {upper_limit}!')
                    continue
            return res


def get_comp_number(lower_limit, upper_limit):
    res = randint(lower_limit, upper_limit)
    print(f'Hint: {res}')
    return res


def compare_numbers(comp_number, user_number):
    if comp_number == user_number:
        print('Congratulations!')
        return True
    elif abs(comp_number - user_number) <= 2:
        print('Hot')
    elif abs(comp_number - user_number) <= 4:
        print('Warm')
    else:
        print('Cold')
        return False


def game_guess_number():
    lower_limit = 0
    upper_limit = 9

    max_attempts = 4
    attempts = 0

    comp_number = get_comp_number(lower_limit, upper_limit)

    while attempts < max_attempts:
        attempts += 1

        user_number = get_user_number(f'Guess the number [{lower_limit}-{upper_limit}],attempts {attempts}/{max_attempts}', lower_limit, upper_limit)

        if compare_numbers(comp_number, user_number):
            break
        if attempts == max_attempts:
            print(f'You run out of attempts, the correct number was {comp_number}')
        else:
            print('Try again!')


game_guess_number()
