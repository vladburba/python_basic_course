answer = 100

while answer <= 0 or answer >= 10:
    answer = int(input("Введите число больше ноля и меньше 10: "))
    print('Answere= ',answer)
    if 0 < answer < 10:
        print(answer,"Ваше число удовлетворяет условиям.")
        print(" Сейчас мы его возведем в квадрат и ты проверишь результат!")
        answer=answer**2
        print(" Результат: ", answer)
        break
    else:
        print("Неправильный ответ попробуй ещё раз, пожулуйста!")
print(answer)