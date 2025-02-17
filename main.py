"""импортирую библиотеку randint."""
from random import randint


# Новый импорт.
# Из модуля start_game_banner, который расположен в папке graphic_arts,
# импортируем функцию run_screensaver().
from graphic_arts.start_game_banner import run_screensaver


def attack(char_name: str, char_class: str) -> str:
    """Функция атака."""
    if char_class == 'warrior':
        return (f'{char_name} нанёс противнику урон {5 + randint(3, 5)}')
    if char_class == 'mage':
        return (f'{char_name} нанёс противнику урон {5 + randint(5, 10)}')
    if char_class == 'healer':
        return (f'{char_name} нанёс противнику урон {5 + randint(-3, -1)}')


def defence(char_name: str, char_class: str) -> str:
    """Функция защита."""
    if char_class == 'warrior':
        return (f'{char_name} блокировал {10 + randint(5, 10)} ед. урона')
    if char_class == 'mage':
        return (f'{char_name} блокировал {10 + randint(-2, 2)} ед. урона')
    if char_class == 'healer':
        return (f'{char_name} блокировал {10 + randint(2, 5)} ед. урона')


def special(char_name: str, char_class: str) -> str:
    """Функция специальное умение."""
    if char_class == 'warrior':
        return (f'{char_name} применил умение «Выносливость {80 + 25}»')
    if char_class == 'mage':
        return (f'{char_name} применил умение «Атака {5 + 40}»')
    if char_class == 'healer':
        return (f'{char_name} применил умение «Защита {10 + 30}»')


def start_training(char_name: str, char_class: str) -> str:
    """Функция начать тренировку."""
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — великий мастер ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
    print('Потренируйся управлять своими навыками.')
    print('Команды: attack - атака, defence - блок и special — суперсила.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd: str = None
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class() -> str:
    """Функция свыбор класса."""
    approve_choice: str = None
    char_class: str = None
    while approve_choice != 'y':
        char_class = input('Класс: Воин- warrior, Маг- mage, Лекарь- healer')
        if char_class == 'warrior':
            print('Воитель — воин ближнего боя.')
        if char_class == 'mage':
            print('Маг — находчивый воин дальнего боя.')
        if char_class == 'healer':
            print('Лекарь — могущественный заклинатель.')
        approve_choice = input('(Y)выбор, любая др. кнопка - отмена').lower()
    return char_class


def main() -> str:
    """Начало."""
    if __name__ == '__main__':
        run_screensaver()
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: str = choice_char_class()
    print(start_training(char_name, char_class)) 


main()
