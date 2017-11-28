import os

migrations = 'Migrations'
current_dir = os.path.dirname(os.path.abspath(__file__))
files_directory = os.path.join(current_dir, migrations)

files = os.listdir(files_directory)

sql_file_list = list()
for file in files:
    file_list = file.split(".")
    if 'sql' in file_list:
        sql_file_list.append(file)


search_list_1 = set()
password = input('придумайте пароль для выхода')
while True:
    world = input('введите слово, которое вы ищите или команду для выхода из программы')
    if world == password:
        break
    if __name__ == '__main__':
        for file in sql_file_list:
            with open(os.path.join(files_directory, file)) as f:
                file_information = f.read()
                if world in file_information:
                    search_list_1.add(file)


    sql_file_list = set(sql_file_list)
    sql_file_list = set(sql_file_list & search_list_1)
    sql_file_list = list(sql_file_list)
    print(sql_file_list)
    print("Всего:",len(sql_file_list))
    search_list_1.clear()

print("Надеюсь вы нашли то, что хотели")
