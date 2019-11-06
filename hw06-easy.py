# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

class TownCar:
    def __init__(self, Towncar_model):
        self.model = TownCar_model
        self.speed = 100
        self.color = col_red
        self.name = name_qwe
        self.is-police = False
        self.go()
        self.stop()
        self.turn()


    def go(self):
        print(self.model, 'go')

    def stop(self):
        print(self.model, 'loading')

    def get_serial_number(self):
        return self._serial_number


# student2 = {
# "name" : "Александр",
# "surname" : "Иванов",
# "birth_date" : '10.11.1998',
# "school" : "8 гимназия",
# "class_room" : "5 А"
# }
# Потом возникает необходимость изменять и обрабатывать данные каждого студента, для этих задач
# вы начинаете писать функции.
# но функция - не очень удобное решение
def next_class ( current_class ):
    return str ( int ( current_class . split ()[ 0 ]) + 1 ) + ' ' + current_class . split ()[ 1]
# т.к. количество функций постоянно увеличивается
def change_class ( current_class ):
    pass

current_class.split ()[0]