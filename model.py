import random


def get_contact():
    id = random.randint(100, 999)
    name = input('ФИО: ')
    phone = input('Телефон: ')
    post = input('Должность: ')
    salary = input('Зарплата: ')

    return f'{id} || {name} || {phone} || {post} || {salary} \n'


def find_contact(book: list, req: str) -> str:
    a = ''
    for i in book:
        if i.find(req) != -1:
            a += f'{i}'
    if a == '':
        return 'Пусто!'
    else:
        return a


def get_request():
    return input('Введите для поиска: ')


def choose_mode():
    return int(input('Режим записи - 1 ; Режим поиска - 2 ; Режим редактирования - 3 '))


def editing(mass):
    a = input('Введите для редактирования: ')
    staff = []
    index = 0
    for i in range(len(mass)):
        if mass[i].find(a) != 1:
            staff = mass[i].split('||')
            print(staff)
            index = i
    print(f'Выберите атрибут для редактирования: \n \
            {staff[1]} - 1 \n \
            {staff[2]} - 2 \n \
            {staff[3]} - 3 \n \
            {staff[4]} - 4 \n ')
    atribute = int(input())
    staff[atribute] = input('Новое значение: ')
    staff = ' || ' .join(staff)
    mass[index] = staff
    return mass
