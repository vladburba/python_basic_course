# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
# list1 = [1, 2, 4, 0]
# list2 = [el ** 2 for el in list1]
# print(list2)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

# list_a = ['cardamon', 'apple', 'banana', 'melon', 'papaya', 'kiwi', 'orange', 'mango', 'ananas', 'cherry',
#           '5', '6', '7']
# list_b = ['apple', 'banana', 'melon', 'papaya', 'kiwi', 'orange', 'mango', 'strawberry', '6', '7', '8']
# list_a = list_b + list_a
# list_c = []
# for a in list_a:
#     for b in list_b:
#         if a == b:
#             list_c.append(a)
#             break
# print(list_c)
# list_c = sorted(list(set(list_c)))
# print(list_c)

# numbers = [i for i in range(1, 11) if i % 2 == 0]

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
#
# numbers = [i for i in range(-24, 24)]
# print(numbers)
# numbers2 = [el for el in numbers if el % 3 == 0 and el > 0 and el % 4 != 0]
# print(numbers2)
