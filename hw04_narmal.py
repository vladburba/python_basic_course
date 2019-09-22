# Задача - 1
# Запросите у пользователя имя, фамилию, email. Теперь необходимо совершить проверки, имя и фамилия должны иметь
# заглавные первые буквы.
# email - не должен иметь заглавных букв и должен быть в формате: текст в нижнем регистре,
# допускается нижнее подчеркивание и цифры, потом @, потом текст, допускаются цифры, точка, ru или org или com.
# Например:
# Пупкин василий - неверно указано имя, te$T@test.net - неверно указан email
# (спецсимвол, заглавная буква, .net), te_4_st@test.com - верно указан.
import re

pattern = '[A-Z][a-z]+'

while True:
    name = input('Input your name: ')
    if (re.match(pattern, name)): break
while True:
    surname = input('Input your surname: ')
    if (re.match(pattern, surname)): break

pattern = '[a-z,_0-9]+@[a-z]+\.(ru|org|com)'

while True:
    email = input('Input your email: ')
    if (re.match(pattern, email)): break

print('Thanks that\'s all right')
print('Task1_finished')
