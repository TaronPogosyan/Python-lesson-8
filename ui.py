# Создать иформационную систему позволяющую работать с сотрудниками некой компании \ студентами вуза \ учениками школы.


from model import add_database, find_database, changes_database
from logger import write_database, read_database, rename_data, write_re


print('Выберите режим работы с данными сотрудников: ')
print('1. Внести данные нового сотрудника\n2. Поиск данных сотрудника по базе\n3. Вывести всех сотрудников на экран\n4. Внести изменения')
mode = int(input())
if mode == 1:
    a = add_database()
    write_database(a)

elif mode == 2:
    print(find_database(read_database()))

elif mode == 3:
    print(read_database())

elif mode == 4:
    mass = read_database()
    write_re(changes_database(mass))

else:
    print('Введено неверное значение!')