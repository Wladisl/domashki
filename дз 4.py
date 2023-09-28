# Task 1. Дана довільна строка. Напишіть код, який знайде в ній і виведе на екран кількість слів, які містять дві голосні літери підряд.
string = input('Enter words: ')
vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']  
words = string.split()
count = 0
for word in words:
    has_vowels_in_a_row = False
    for i in range(len(word) - 1):
        if word[i] in vowels and word[i+1] in vowels:
            has_vowels_in_a_row = True

    if has_vowels_in_a_row:
        count += 1
print(f'Кількість слів, які містять дві голосні літери підряд: {count}')

# Task 2. Є два довільних числа які відповідають за мінімальну і максимальну ціну.
# Є Dict з назвами магазинів і цінами: { "cito": 47.999, "BB_studio" 42.999, "momo": 49.999, "main-service": 37.245, "buy.now": 38.324, "x-store": 37.166, "the_partner": 38.988, "store": 37.720, "rozetka": 38.003}.
# Напишіть код, який знайде і виведе на екран назви магазинів, ціни яких попадають в діапазон між мінімальною і максимальною ціною. Наприклад:
# lower_limit = 35.9
# upper_limit = 37.339
# > match: "x-store", "main-service"

lower_limit = 35.9
upper_limit = 37.339

shops_and_prices = {
    'cito': 47.999,
    'BB_studio': 42.999,
    'momo': 49.999,
    "main-service": 37.245,
    'buy.now': 38.324,
    'x-store': 37.166,
    "the_partner": 38.988,
    "store": 37.720,
    "rozetka": 38.003

}
match_shop = []
for shop, price in shops_and_prices.items():
    if lower_limit <= price <= upper_limit:
        match_shop.append(shop)
if match_shop:
    print(f'Match:{match_shop}')
else:
    print('Nothing')

