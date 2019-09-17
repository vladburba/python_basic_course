# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random
import random

list_numbers = []
num = 1
last_number = int(input("Введите число элементов списка: "))
result = f'num = {num} last_num = {last_number} list_numbers {list_numbers} '
print(result)

while num <= last_number:
    leaf = random.randint(-100, 100) #- случайное целое число N, A ≤ N ≤ B
    list_numbers.append(leaf)
    num += 1
print(list_numbers)
print('Task_3_is_finished')
print()

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

first = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4]
second = first
third = []
print(first)
for f in first:

    print('f = ', f)
    for s in second:
        if f == s:
            second.remove(s)
            third.append(f)
print(third)
# print(first)