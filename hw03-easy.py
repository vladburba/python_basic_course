# Задание - 1
# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"
#
def logpip(name, age, town):
     # str = name+age+town
     result = f'Name = {name} Age = {age} Town =  {town} '
     return result
name = input('Input name: ')
age = input('Input age: ')
town = input('Input towon: ')
print(logpip(name,age,town))
print('Task_1_finished')

# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них

# def mymax(a,b,c):
#     if a >=b and a >=c:
#         mmax = a
#         return mmax
#     elif b >= a and b >= c:
#         mmax = b
#         return mmax
#     elif c >= a and c >= b:
#         mmax = c
#         return mmax
# a = int(input('Input First: '))
# b = int(input('Input Second: '))
# c = int(input('Input Third: '))
# print('Max = ', mymax(a,b,c))
# print('Task_2_finished')

# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов


def func(*args):
    print(args)
    print(type(args))
    # print(name)
    mymax = 0
    for str in args:
        teclen = len(str)
        if teclen >= mymax:
            mymax = teclen
    return mymax

print('Максимальная длина строки = ',func('Ivan', '10fgfg', '1sdsdg', '2sdfsdf', '3', '5', '4','sdgsdgdfgdgsdgsdgsdgsd'))