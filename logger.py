def write_database(a):
    with open('Python DZ 8/database.txt', 'a', encoding='utf=8') as f:
        f.write(f'{a}\n')

def read_database():
    mass = []
    with open('Python DZ 8/database.txt', 'r', encoding='utf=8') as f:
        for i in f:
            mass.append(i)

        return mass


def rename_data(mass):
    with open('Python DZ 8/database.txt', 'w', encoding = 'utf=8') as f:
        for i in mass:
            f.write(i)

def write_re(a):
    with open('Python DZ 8/database.txt', 'w', encoding='utf=8') as f:
        for i in a:
            f.write(i+'\n')
        