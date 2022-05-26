import psycopg2
from psycopg2 import Error
import time
import numbers

try:
    # Подключение к существующей базе данных
    user, password, host = input('Enter user: '), input('Enter pqssword: '), input('Enter host: ')
    port, database = input('Enter port: '), input('Enter database: ')
    connection = psycopg2.connect(user=user,
                                  password=password,
                                  host=host,
                                  port=port,
                                  database=database)
    # Курсор для выполнения операций с базой данных
    cursor = connection.cursor()
    # Распечатать сведения о PostgreSQL
    print("Информация о сервере PostgreSQL \n",connection.get_dsn_parameters(), "\n")
    # Выполнение SQL-запроса
    cursor.execute("SELECT version();")
    # Получить результат
    record = cursor.fetchone()
    print("Вы подключены к: \n", record, "\n")
    cursor.connection.cursor()
    def tables():
        sql = "SELECT table_name FROM information_schema.tables WHERE table_schema='public'"
        cursor.execute(sql)
        tables = cursor.fetchall()
        print(tables, '\n')
        return tables


    def create_table():
        qry = input("Создать таблицу? y/n \n")
        if qry == 'n':
            return
        elif qry == 'y':
            nam_table = input("Введите имя таблицы: ")
            title_table = input("Введите параметры столбцов соблюдая синтаксис psql: ")
            cursor.execute(f"""CREATE TABLE IF NOT EXISTS {nam_table} ({title_table});""")
            connection.commit()
            print("Table created \n")
            return connection.commit()
        else:
            print('Error \n')
            create_table()


    def query():
        qry = input("Create request? y/n: \n")
        if qry == 'n':
            return
        elif qry == 'y':
            resp = input("Enter your request: \nSELECT ")
            try:
                if ';' in resp:
                    cursor.execute('SELECT ' + resp)
                    print("Result: ", cursor.fetchall(), "\n")
                else:
                    cursor.execute('SELECT ' + resp + ';')
                    print("Result: ", cursor.fetchall(), "\n")
                return
            except (Exception, Error) as error:
                print(">>> [!] Error, ", error)
                return


    def insert_data():
        try:
            table = input('Enter table name: ')
            cursor.execute(f"SELECT * FROM {table} LIMIT 0;")
            colnames = [desc[0] for desc in cursor.description]
            print('Введите значения соответственно: ', colnames)
            count = 0
            lst_val = []
            for  num, names in enumerate(colnames):
                names = input(f'Enter value {colnames[count]}: ')
                if colnames[0].isdigit() == True:
                    names = int(names)
                lst_val.append(names)
                count += 1

            cursor.execute(f"""INSERT INTO {table} VALUES {tuple(lst_val)};""")
            connection.commit()
            print('Данные добавлены. \n')
            return connection.commit()
        except:
            print('>>> [!] This table not found.\n')
            insert_data()


    while True:
        time.sleep(2)
        action = input("\nВыберите действие. \nПоказать все таблицы: st \nСоздать таблицу: ct \nВнести данные в таблицу: ii \nПолучить данные: s \nВыход: q\n")
        if action == "q":
            break
        elif action == "st":
            tables()
        elif action == "ct":
            create_table()
        elif action == "ii":
            insert_data()
        elif action == "sf":
            query()
        else:
            print("Error")


except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")
