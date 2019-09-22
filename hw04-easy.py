# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

list1 = [1, 4, 10, 15, 30, 11, 18, 22, 13, 7, 8, 9, 10, 27, 30, 49, -8, 10, 0, -75]
list2 = []

print(list1)
list2 = list((map(lambda x: x*x, list1)))
print(list2)
print('Task1_finished')

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

list_a = ['cardamon', 'apple', 'banana', 'melon', 'papaya', 'quiwi', 'orange', 'mango', 'ananas', 'cherry','5','6','7']
list_b = ['topinambur', 'apple', 'banana', 'melon', 'papaya', 'quiwi', 'orange', 'mango', 'strawberry', '6','7' ,'8']
list_c = []

for b in list_b:
     if b in list_a:
        list_c.append(b)
print(list_a)
print(list_b)
print(list_c)
print('Task2_finished')

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
result = [i for i in range(-20, 21)]
print(result)

result = [res for res in result if res > 0 and res % 3 == 0 and res % 4 != 0]
print(result)

