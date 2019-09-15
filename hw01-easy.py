print("Привет, программист!")
name = input("Введите ваше имя: ")
print(name, ", добро пожаловать в мир Python!")
a,b,c, = 1,2,3
print('a,b,c =',a,b,c)
a,b,c = 3,2,1
print('a,b,c =',a,b,c)
print('Task 1 is finished')
do = int(input("Введите число: "))
print('Вы ввели число: ', do, 'прибавим к нему 2')
do = do + 2
print('Результат равен: ', do)
print('Task 2 is finished')
age = int(input('Введите ваш возраст:'))
if age >= 18:
    print("Доступ разрешен")
else:
    print("Извините, пользование данным ресурсом только с 18 лет")
print('Task 3 is finished')