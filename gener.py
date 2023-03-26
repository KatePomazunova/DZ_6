import sqlite3



queries = {
    '1': 'query_1.sql',
    '2': 'query_2.sql',
    '3': 'query_3.sql',
    '4': 'query_4.sql',
    '5': 'query_5.sql',
    '6': 'query_6.sql',
    '7': 'query_7.sql',
    '8': 'query_8.sql',
    '9': 'query_9.sql',
    '10': 'query_10.sql'
}


def options():
    print('''
    1. Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
    2. Знайти студента із найвищим середнім балом з певного предмета.
    3. Знайти середній бал у групах з певного предмета.
    4. Знайти середній бал на потоці (по всій таблиці оцінок).
    5. Знайти які курси читає певний викладач.
    6. Знайти список студентів у певній групі.
    7. Знайти оцінки студентів у окремій групі з певного предмета.
    8. Знайти середній бал, який ставить певний викладач зі своїх предметів.
    9. Знайти список курсів, які відвідує студент.
    10. Список курсів, які певному студенту читає певний викладач.
    exit - вийти.
    ''')


def execute_query(sql_file: str) -> list:
    sql = ''
    with open(sql_file, 'r') as q:
        sql = q.read()
    with sqlite3.connect('dz6') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


def main():
    command = input("enter query's number or 'help'/ 'exit'\n >>>  ")
    while command != 'exit':
        if command in queries:
            print(execute_query(queries[command]))
        else:
            options()
        command  = input('>>>')



if __name__ == '__main__':
    main()