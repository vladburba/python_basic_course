# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
print('os.name = ', os.name)
print('os.getcwd() = ', os.getcwd())
new_dir = input('Input name new dir: ')
dir_path = os.path.join(os.getcwd(), new_dir)
print('NewDir = ', dir_path)
try:
    os.mkdir(dir_path)
except FileExistsError:
    print('Такая директория уже существует')
print('Task1_finished')

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.