# TaSK. AI порграма має відповісти на питання чи є введений стрінг
# 1 - номер телефону
# 2 - email
# 3 - Name
#
# +380631112233 -> Phone
# bcdef@abc.efg -> email   3+ letters @ 3 letters. 3 letters
# Bill J.I. -> name   2 words
# something else -> unknown


raw_string = ''

email_parts = raw_string.split('@')  # розділили по символу '@' щоб можно було у разі введення емейлу перевірку зробити по частинам до нашого символу і після
result = 'Unknown'

phone_conditions = (
    len(raw_string) == 13,
    raw_string[0] == '+',
    raw_string[1:].isdigit(),
    raw_string[3:6] in ('050', '066', '095', '099', '063', '073', '093', '070', '700', '090', '900', '067', '068', '096', '097', '098', '091', '092', '020', '089', '094', '039')
)

if all(phone_conditions):
    result = 'Phone Number'

elif len((splited := raw_string.split(' '))) == 2:
    _name = splited[0]
    _initials = splited[1]
    if _name.isalpha() and _name.capitalize() == _name:
        if _initials[-1] == '.' and _initials[-3] == '.' and _initials[0].isalpha() and _initials[0].upper() == _initials[0] and _initials[2].isalpha() and _initials[2].upper() == _initials[2]:
            result = 'Name'

elif len(email_parts) == 2 and len(email_parts[0]) >= 3 and len(email_parts[1]) == 7 and '.' in email_parts[1]:
    result = 'Email'
print(result)
