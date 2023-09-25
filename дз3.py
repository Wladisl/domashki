# Task 1. Напишіть код, який зформує строку, яка містить певну інформацію про символ за його номером у слові.
# Наприклад "The [номер символу] symbol in '[тут слово]' is '[символ з відповідним порядковим номером в слові]'". Слово та номер символу отримайте за допомогою input() або скористайтеся константою.
# Наприклад (слово - "Python" а номер символу 3) - "The 3 symbol in 'Python' is 't' ".

while True:
    word = input("Enter a word: ")
    if word.isalpha():  # перевірка на те чи ялвяється те що ми ввели словом
        break
    else:
        print("Enter a word not something else")
index = int(input("Enter the symbol number: "))
if 1 <= index <= len(word):
    result = f"The {index} symbol in '{word}' is '{word[index - 1]}'"  # задали довжину нашу таким чином щоб у разі якщо ввели одну букву,вона видавалась як перша а не помилка
    print(result)
else:
    print("The character number exceeds the word length.")

# Task 2. Вести з консолі строку зі слів за допомогою input() (або скористайтеся константою).
# Напишіть код, який визначить кількість слів, в цих даних.

words_string = input('Enter a string of words: ')
word = words_string.split()
words_count = len(word)
print(f'The number of words in the entered line: {words_count}')

# Task 3. Існує ліст з різними даними, наприклад lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який сформує новий list (наприклад lst2), який би містив всі числові змінні (int, float), які є в lst1.
# Майте на увазі, що данні в lst1 не є статичними можуть змінюватись від запуску до запуску.

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = []
for lst_item in lst1:
    if type(lst_item) in (int, float):
        lst2.append(lst_item)
print(lst2)
