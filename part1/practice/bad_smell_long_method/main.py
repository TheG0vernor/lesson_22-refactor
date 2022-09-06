# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля


csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def get_users_list():
    data = _read(csv)
    data = _sort(data)
    return _filter(data)


    # Чтение данных из строки
def _read(file):
    list_ = []
    f = file.split('\n')
    for i in f:
        list_.append(i.split(';'))
    return list_


    # Сортировка по возрасту по возрастанию
def _sort(read):
    return sorted(read, key=lambda func: int(func[1]))


    # Фильтрация
def _filter(sort_):
    list_ = []
    for i in sort_:
        if i[1].isdigit():
            if int(i[1]) > 10:
                list_.append(i)
    return list_


if __name__ == '__main__':
    print(get_users_list())
