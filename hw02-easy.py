# Задача-1:
fruits = ["яблоко", "банан", "киви", "арбуз"]
i=0

for fruit in fruits:# переменной fruit при каждой итерации(полном обороте) цикла присваиваются элементы поочереди
    i +=1
    # result = '{}. {}'.format(i,fruit)
    result2 = '{:>10}'.format(fruit)
    print(i,result2)
    # result = f'{i}. {fruit}'
    # print(result)
print('Task_1_is_finished')
print()


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

fruits1 = ["дыня", "яблоко", "банан", "лимон", "киви", "грецкий орех", "арбуз", "инжир", "финики", "арахис"]
fruits2 = ["яблоко", "банан", "киви", "арбуз", "жигули"]
print(fruits1)
print(fruits2)
for fruit2 in fruits2:# переменной fruit при каждой итерации(полном обороте) цикла присваиваются элементы поочереди
    for fruit1 in fruits1:
        if fruit2 == fruit1:
            fruits1.remove(fruit1)
    # print(result)
print(fruits1)
# print(fruits2)
print('Task_2_is_finished')
print()


# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
numbers1 = [1,3,7,10,15,26,37,48,54,69,17,100,50,11,99,114,0,112,112,18,19,29,21,25,94,46,16,15]
numbers2 = []

for numb in numbers1:
    if numb % 2 == 0:
        result3 = numb / 4
        numbers2.append(result3)
    else:
        result3 = numb * 2
        numbers2.append(result3)
print(numbers1)
print(numbers2)
print('Task_3_is_finished')
print()