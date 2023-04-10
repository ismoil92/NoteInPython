from ClassNumberOne import Note as note
from datetime import datetime as dt
from CSVClass import CRUD_CSV as csv



def add_in_csv():
    data1 = note()
    data1.set_header("Python")
    data1.set_note_body("Изучение языка python")
    data1.set_date_time(dt.now())
    add = csv()
    add.write_file_csv(data1)


def read_from_csv():
    read = csv();
    read.read_file_csv()


print("1-Добавление\n2-Чтение")
select_number = int(input("Выберите номер команд:"))
if select_number == 1:
    add_in_csv()
elif select_number == 2:
    read_from_csv()
