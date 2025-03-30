import datetime

BAD_WORDS = 'редиска', 'сосиска', 'репка'
registration = {"Фамилия": "", "Имя": "", "Логин": "", "Пароль": ""} 
news = {"ФИО": "", "Заголовок статьи": "", "Текст": ""} #это словарь
def spy_bad_words(data):
    '''Эта функция сначала получает информацию в переменнную data
    с помощью метода split разбивает по словам информацию, полученную в data
    с помощью цикла перебираем элементы списка data_list и, используя условную конструкцию, проверяем наличие плохих или хороших слов
    функция возвращает либо true либо false (return flag)''' 
    data_list = data.split(' ') # data_list это список, полученнный из строки data, которая была разделена методом split по пробелу
    flag = True
    for i in data_list:
        if i.lower() in BAD_WORDS:
            print(f'Нашли плохое слово {i}')
            flag = False
            break
    return flag # функция возвращает flag
#data в spy_bad_words(data) и data в final_result(data) это разные переменные, каждая работает в пределах одной функции

def spy_zero_str(data):
    flag = True
    data = data.strip()
    if data == "":
        flag = False
    return flag


def final_result(data):
    run = True
    while run:
        info = input(data)
        result_zero = spy_zero_str(info)
        if result_zero == False:
            continue

        result = spy_bad_words(info) # В result получаем информацию о том, нет ли в info (вводимых пользователем данных) плохих слов
        #  В result попадет либо True либо False
        if result == True:
            if "Введите ФИО:" in data: #если функция вызывается с аргументом, содержащим 'Введите ФИО: ', то происходит
        #запись введенных данных в словарь news с ключом ФИО
                news["ФИО"] = info
            elif "Введите Заголовок статьи" in data:
                news["Заголовок статьи"] = info
            elif "Введите Текст" in data:
                news["Текст"] = info
            elif "Введите Фамилию" in data:
                registration["Фамилия"] = info
            elif "Введите Имя" in data:
                registration["Имя"] = info 
            elif "Введите Логин" in data:
                registration["Логин"] = info   
            elif "Введите Пароль" in data:
                registration["Пароль"] = info          
            run = False      
# date = '19.01.2025'
# time = '11:30'
final_result('Введите Фамилию: ') # здесь и далее final_result(data = 'Введите Фамилию: ') запись информации в словарь - функция 
#записывает проверенную информацию в словари news и registration
final_result('Введите Имя: ')
final_result('Введите Логин: ')
final_result('Введите Пароль: ')
print(registration)
final_result('Введите ФИО: ') 
final_result('Введите Заголовок статьи: ')
final_result('Введите Текст: ')

current_date = datetime.datetime.now()
# print(current_date)
# str_current_date = str(current_date)
# print(str(current_date))
news["Дата"] = current_date.strftime("%d-%m-%Y")  #str_current_date[0:10]
news["Время"] = current_date.strftime("%H:%M") #str_current_date[11:16]
print(news)

# run = True
# while run:
#       author = input('Введите свое ФИО ')
#       result = spy_bad_words(author)
#       print(result)
#       if result == True:
#           run = False   

# print(spy_bad_words(header))
# run = True
# while run:
#       header = input('Введите заголовок статьи ')
#       result = spy_bad_words(header)
#       print(result)
#       if result == True:
#           run = False 
# run = True
# while run:
#       text = input('Текст: ')
#       result = spy_bad_words(text)
#       print(result)
#       if result == True:
#           run = False 



count_like = 0
donat = 0
status = True
# header_list = header.split(' ')
# for i in header_list:
#     if i.lower() in BAD_WORDS:
#         print(f'Нашли плохое слово {i}')
#         break
# text_list = text.split(' ')
# for i in text_list:
#     if i.lower() in BAD_WORDS:
#         print(f'Нашли плохое слово {i}')
#         break

