"""
    opening program interface and procces events
"""
import sys
import os
import time


from .storage import (
        add_new_event,
        get_path_resource,
        get_events_by_status,
        edit_event,
        initialize,
        connect
        )


get_connection = lambda:connect(get_path_resource('cool_diary.sqlite'))


def agreed(question):
    answer = input('{}(Да/y): '.format(question))
    return answer.lower() == 'да' or answer.lower() == 'y'


def show_edit_events(status, text, sleep=0):
    events = get_events_by_status(get_connection(), status)
    id_lst = {}
    counter = 1
    for i in events:
        id_lst[str(counter)] = i
        print('{}. C {} до {} назначено: "{}"'.format(counter, i[2], i[3], i[1]))
        counter += 1
    data = id_lst.get(input(text))
    if not data:
        print('Неверно введенные данные.')
        time.sleep(sleep)
        return None
    return data


def event0():
    if agreed('Закрыть ежедневник?'):
        sys.exit(0)


def event1():
    data = show_edit_events(1, 'Нажмите любую кнопку для возврата...')
    if data:
        edit_event(get_connection(), data, event_type)


def event2():
    name = input('Введите название события: ')
    begin_date = input('Введите дату начала события (гггг-мм-дд): ')
    end_date = input('Введите дату окончания события (гггг-мм-дд): ')
    if not name or not end_date:
        print('Неверно введены данные')
        time.sleep(2)
        return
    print('Вы указали:', name, begin_date, end_date)
    if agreed('Сохранить?'):
        add_new_event(get_connection(), (name, begin_date,end_date))
        print('Запись сохранена.')
        temp = input('Нажмите любую кнопку...')


def event3(): # edit
    data = show_edit_events(1, 'Введите номер задачи для редактирования: ', 1)
    if not data:
        return
    tmp_lst = []
    for i in range(1,4):
        new = input('Старая запись: "{}",\nВведите новую или не изменяйте: '.format(data[i]))
        tmp_lst.append(data[i] if new == '' else new)
    tmp_lst.append(data[4])
    tmp_lst.append(data[0])

    edit_event(get_connection(), tuple(tmp_lst))


def event4(): #end
    data = show_edit_events(1, 'Введите номер задачи для завершения: ', 1)
    if data:
        tmp_lst = list(data)[1:5]
        tmp_lst[3] = 0
        tmp_lst.append(data[0])
        edit_event(get_connection(), tuple(tmp_lst))


def event5(): # restart
    data = show_edit_events(0, 'Введите номер задачи для повторения: ', 1)
    if data:
        tmp_lst = list(data)[1:5]
        tmp_lst[2] = input('Введите дату окончания события (гггг-мм-дд): ')
        tmp_lst[3] = 1
        tmp_lst.append(data[0])
        edit_event(get_connection(), tuple(tmp_lst))


EVENTS = {
            '0': event0,
            '1': event1,
            '2': event2,
            '3': event3,
            '4': event4,
            '5': event5,
        }


def get_menu():
    menu_dict = {
        '0': 'Выход',
        '1': 'Вывести список задач',
        '2': 'Добавить задачу',
        '3': 'Отредактировать задачу',
        '4': 'Завершить задачу',
        '5': 'Начать задачу сначала',
    }
    return menu_dict


def show_welcome():
    with open(get_path_resource('welcome.txt')) as f:
        for i in f:
            print(i.rstrip())


def clear_console():
    if sys.platform=='win32':
        os.system('cls')
    else:
        os.system('clear')
    pass


def show_menu():
    clear_console()
    show_welcome()
    print('Выберите действие:\n')
    menu = get_menu()
    for item in sorted(menu):
        if item != '0':
            print(''.join([item, '.']),menu.get(item))
    print(''.join(['0', '.']),menu.get('0'))

    print('\n')


def main():
    initialize(get_connection())
    while True:
        show_menu()
        answer = input('\nВыберите пункт меню: ')
        event = EVENTS.get(answer)
        if event:
            event()
        else:
            print('Неверная команда')
            time.sleep(1)


if __name__ == '__main__':
    main()


