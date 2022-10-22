# Добавляем контакт
def add_database():
    id = input('Введите ID сотрудника: ')
    last_first_middle = input('Введите ФИО сотрудника: ')
    phone = input('Введите номер телефона сотрудника: ')
    post = input('Введите должность сотрудника: ')
    salary = input('Введите заработную плату: ')
    return (f'{id} || {last_first_middle} || {phone} || {post} || {salary}\n')

# Поиск контакта
def find_database(f):
    a = input('Введите данные для поиска: ')
    findC = list(filter(lambda x: a in x, f))
    return findC

def changed_database():
    id = input('Введите ID сотрудника: ')
    last_first_middle = input('Введите ФИО сотрудника: ')
    phone = input('Введите номер телефона сотрудника: ')
    post = input('Введите должность сотрудника: ')
    salary = input('Введите заработную плату: ')
    return (f'{id} || {last_first_middle} || {phone} || {post} || {salary}\n')


def changes_database(mass):
    findC = find_database(mass)
    index = mass.index(findC[0])
    mass[index] = changed_database()
    return mass
    # print(findC)


