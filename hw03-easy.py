# Задание - 1
# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"

def logpip(name, age, town):
    # str = name+age+town
    result = f'Name = {name} Age = {age} Town =  {town} '
    return result
name = input('Input name: ')
age = input('Input age: ')
town = input('Input towon: ')
print(logpip(name,age,town))