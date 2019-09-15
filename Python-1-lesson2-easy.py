fruits = ["яблоко", "банан", "киви", "арбуз"]
i=0

for fruit in fruits:# переменной fruit при каждой итерации(полном обороте) цикла присваиваются элементы поочереди
    i +=1
    # print('{}. {}'.format(i,fruit))
    result = f'{i}. {fruit}'
    print(result)
print('Task_1_is_finished')  # Просто пустая строка, для удобства чтения вывода

