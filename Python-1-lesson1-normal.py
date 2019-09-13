answer = 100

while answer <= 0 or answer >= 10:
    answer = int(input("Введите число больше ноля и меньше десяти: "))
    print('Answer= ',answer)
    if 0 < answer < 10:
        print(answer,"Ваше число удовлетворяет условиям.")
        print(" Сейчас мы его возведем в квадрат и увидим результат!")
        answer=answer**2
        print(" Результат: ", answer)
        break
    else:
        print("Неправильный ответ попробуй ещё раз, пожулуйста!")
print(answer)
print('Task_1_is_finished')
number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))
print('number1',number1)
print('number2',number2)
if number1 == number2:
    print("Переменные равны менять смысла нет")
elif number1 > number2:
    number1 = number1 - number2
    number2 = number2 + number1
    number1 = number2 - number1
    print('number1', number1)
    print('number2', number2)
else:
    number2 = number2 - number1
    number1 = number1 + number2
    number2 = number1 - number2
    print('number1', number1)
    print('number2', number2)
print('Task_2_is_finished')