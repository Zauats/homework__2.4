import os

migrations = 'Migrations'
current_dir = os.path.dirname(os.path.abspath(__file__))
files_directory = os.path.join(current_dir, migrations)

files = os.listdir(files_directory)


def file_sql_list():
    sql_file_list = list()
    for file in files:
        file_list = os.path.splitext(file)
        if '.sql' == file_list[1]:
            sql_file_list.append(file)
    return sql_file_list






def search_list(Your_list):
    search_list = list()
    for file in Your_list:
        with open(os.path.join(files_directory, file)) as f:
            file_information = f.read()
            if world in file_information:
                search_list.append(file)
    return search_list



if __name__ == '__main__':
    sql_file_list = file_sql_list()

    password = input('придумайте пароль для выхода')
    while True:
        world = input('введите слово, которое вы ищите или команду для выхода из программы')
        if world == password:
            break
        else:
            sql_file_list = search_list(sql_file_list)

        for file in sql_file_list:
            print("{}\n".format(file))
        print("Всего файлов найдено:",  len(sql_file_list))

print("Надеюсь вы нашли то, что хотели")
