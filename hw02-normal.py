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
