# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import sys
import shutil

def mydir(dir_path)
    return "I'm func make dir1 - 9 in module lib1"
# print('os.name = ', os.name)
# print('os.getcwd() = ', os.getcwd())
new_dir = input('Input name new dir: ')
dir_path = os.path.join(os.getcwd(), new_dir)
print('NewDir = ', dir_path)
try:
    os.mkdir(dir_path)
except FileExistsError:
    print('Такая директория уже существует')
print('Task1_finished')

dir_path = os.getcwd()
mydir(dir_path)

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
# mypath = os.getcwd()
# cur_dir = os.listdir(path=mypath)
# print(cur_dir)
# onlyfiles = [f for f in cur_dir if os.path.isfile(os.path.join(mypath, f))]
# print(onlyfiles)


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
# print('sys.argv = ', sys.argv)
# file1 = sys.argv[0]
# file2 = file1 + '.copy'
# print(file1, file2)
# shutil.copy(file1, file2)
# print(os.listdir(path=os.getcwd()))