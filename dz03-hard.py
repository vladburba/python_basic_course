# player = {'name': input('Введите имя: '), 'health': 100, 'damage': 50}
# enemy = {'name': input('Введите имя: '), 'health': 100, 'damage': 50}
#
# def attack(who_attack, who_defend):
#     who_defend['health'] -= who_attack['damage']
#     who_defend['health'] = who_defend['health'] - who_attack['damage']

# attack(player, enemy)
# print(enemy['health'], player['health'])

def generate_person_by_name(name, health=100, damage=50, armor=0.7):
    return {'name': name, 'health': health, 'damage': damage, 'armor': armor}

# Описываем функцию для записи нашей структуры в файл.
def write_person_to_file(person):
    with open(person['name'], 'w', encoding='UTF-8') as f:
        for key, value in person.items():
            f.write('{} {}\n'.format(key, value))

# Описываем функцию для получения структуры из файла
def get_person_by_filename(filename):
    person = {}
    with open(filename, encoding='UTF-8') as f:
        for line in f:
            key, value = line.split()
            # Выполняем проверку на ключи, нам ведь нужны конкретные типы данных.
            if key == 'armor':
                value = float(value)
            elif key != 'name':
                value = int(value)
            # Сохраняем значение по ключу.
            person[key] = value
    return person

# Функция для подсчета урона
def calculate_damage(damage, armor):
    return damage // armor

# Функция атаки, принимает на вход 2 структуры
def attack(who_attack, who_defend):
    damage = calculate_damage(who_attack['damage'], who_defend['armor'])
    who_defend['health'] -= damage
    print('{} нанес {} урона {}, у того осталось {} жизней.'.format(who_attack['name'], who_defend['name'], damage,
                                                                    who_defend['health']))


# Создаем наши структуры данных
player_name = input('Введите имя: ')
enemy_name = input('Введите имя: ')

player = generate_person_by_name(player_name)
enemy = generate_person_by_name(enemy_name)
# print(player)
# print(enemy)

# Записываем в файлы наши структуры
write_person_to_file(player)
write_person_to_file(enemy)

# Функция старта игры, никаких аргументов не принимает.
def start_game():
    # получаем наши структуры, через вышеописанную функцию
    player = get_person_by_filename(player_name)
    enemy = get_person_by_filename(enemy_name)
    # Запоминаем кто последний атаковал
    last_attacker = enemy
    while player['health'] > 0 and enemy['health'] > 0:
        if last_attacker == player:
            attack(enemy, player)
            last_attacker = enemy
        else:
            attack(player, enemy)
            last_attacker = player

    if player['health'] > 0:
        print('Игрок победил!')
    else:
        print('Враг победил!')


start_game()
