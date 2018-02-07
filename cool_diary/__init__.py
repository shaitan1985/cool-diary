"""
    opening program interface and procces events
"""
import sys
import os

def event1():
    # here wil be DB query of active events
    for i in range(10):
        print('some actual events')


def event2():
    name = input('Введите название события: ')
    begin_date = input('Введите дату начала события (гггг.мм.дд): ')
    end_date = input('Введите дату окончания события (гггг.мм.дд): ')
    print('Вы указали:', name, begin_date, end_date)
    answer = input('Сохранить?(y)  ')
    if answer.lower() == 'y':
        # here will be saving proc
        print('saved')
        temp = input('Нажмите любую кнопку...')

def event3():
    # here will be  DB query of active events
    # and choosing the number of event
    for i in range(10):
        print('some actual events')

    print('edit')


def event4():
    # here will be  DB query of ended events
    # than the same as create, but with complite value
    for i in range(10):
        print('some actual events')

    print('complite')


def event5():
        # here will be  DB query of ended events
        # and choosing the number of event
    for i in range(10):
        print('some actual events')

    print('rebegin')

EVENTS = {
            '1': event1,
            '2': event2,
            '3': event3,
            '4': event4,
            '5': event5,
        }


def get_menu(step):
    if step == 0:
        menu_dict = {
            '0': 'Выход',
            '1': 'Вывести список задач',
            '2': 'Добавить задачу',
            '3': 'Отредактировать задачу',
            '4': 'Завершить задачу',
            '5': 'Начать задачу сначала',
        }


    return menu_dict


def show_menu(settings):
    print('Ежедневник. Выберите действие:\n')
    menu = get_menu(settings['step'])
    for item in sorted(menu):
        print(''.join([item, '.']),menu[item])
    print('\n')


def procces_event(settings, answer):
    EVENTS[answer]()

def clear_console():
    if sys.platform=='win32':
        os.system('cls')
    else:
        os.system('clear')


def main():
    exit = False
    settings = {'step': 0}
    while not exit:
        clear_console()
        show_menu(settings)
        answer = input()
        if answer == '':
            continue
        if answer == '0':
            exit = True
        else:
            settings['step'] = 1
            procces_event(settings, answer)
        temp = input('Нажмите любую кнопку...')
        settings['step'] = 0



if __name__ == '__main__':
    main()


