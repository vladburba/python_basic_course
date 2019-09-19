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

# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них
def mymax(a,b,c):
    if a >=b and a >=c:
        mmax = a
        return mmax
    elif b >= a and b >= c:
        mmax = b
        return mmax
    elif c >= a and c >= b:
        mmax = c
        return mmax
a = int(input('Input First: '))
b = int(input('Input Second: '))
c = int(input('Input Third: '))
print('Max = ', mymax(a,b,c))