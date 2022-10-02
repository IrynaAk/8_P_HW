# 12, Имя1, Фамилия1, Телефон1, Должность1, 20000
# 13, Имя2, Фамилия2, Телефон2, Должность2, 30000


def max_id():
    with open('Data.txt', 'r', encoding='utf-8') as a:
        data_base = a.readlines()
        max = 0
        for line in data_base:
            data = line.split(', ')
            if int(data[0]) > max:
                max = int(data[0])
    return(max)

# print(max_id())

def add_employee():
    info = ''
    info = info + str(max_id() + 1) + ', '
    last_name = input('Введите фамилию: ')
    info = info + last_name + ', '
    first_name = input('Введите имя: ')
    info = info + first_name + ', '
    phone_number = ''
    valid =False
    while not valid:
        try:
            phone_number = input('Введите номер телефона: ')
            if len(phone_number) != 11:
                print('В номере телефона должно быть 11 цифр.')
            else:
                phone_number = phone_number
                valid = True
        except:
            print('Номер телефона должен состоять только из цифр.')
    info = info + phone_number + ', '
    position = input('Введите должность: ')
    info = info + position + ', '
    salary = ''
    valid =False
    while not valid:
        try:
            salary = input('Введите зарплату в рублях: ')
            if str.isdigit(salary) ==False:
                print('Зарплата должна состоять только из цифр.')
            else:
                valid = True
        except:
            print('Зарплата должена состоять только из цифр.')
    info = info + salary
    return info


def view_data():
    with open('Data.txt', 'rt', encoding='utf-8') as a:
        print(a.read())


def write_data():
    with open('Data.txt', 'a', encoding='utf-8') as a:
        a.write(add_employee())
        a.writelines('\n')

# write_data()


def find_data_surname(surname):
    with open('Data.txt', 'r', encoding='utf-8') as a:
        empl_base = a.readlines()
        for line in empl_base:
            if surname in line:
                print(line)


def find_data_id(empl_id):
    with open('Data.txt', 'r', encoding='utf-8') as a:
        empl_base = a.readlines()
        for line in empl_base:
            if line.startswith(empl_id):
                print(line)



# empl_id = '2'
# find_data_id(empl_id)

 
def edit_data(undifier, current, new_data):
    a = open("Data.txt","r", encoding='utf-8') 
    data_base = a.readlines()
    a.close()
    empl_id = str(undifier)
    a = open("Data.txt","w", encoding='utf-8') 
    for line in data_base:
        if line.startswith(empl_id):
            data = line.split(', ')
            data[current] = new_data
            new_line = ', '.join(data)
            a.write(new_line)
            if current ==5:
                a.write('\n')
        else:
            a.write(line)
    a.close()
    
 
def delete_data(empl_id):
    a = open('Data.txt', 'r', encoding='utf-8')
    d = a.readlines()
    a.close()
    a = open('Data.txt', 'w', encoding='utf-8')
    for line in d:
        data = line.split(', ')
        if data[0] == empl_id:
            print(f'Сотрудник с ID {data[0]} удален')
        else:
            a.write(line)
    a.close()


delete_data('3')


def avg_salary():
    a = open("Data.txt","r", encoding='utf-8') 
    data_base = a.readlines()
    a.close()
    av_sal = []
    for line in data_base:
        data = line.split(', ')
        av_sal.append(int(data[5]))
    return(sum(av_sal)/len(av_sal))
