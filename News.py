import datetime
import re

BAD_WORDS = 'редиска', 'сосиска', 'репка'
regex = '^[A-ZА-ЯЁ]'
pattern = re.compile(regex)
registration = {"Фамилия": "", "Имя": "", "Логин": "", "Пароль": ""} 
news = {"Фамилия Имя": "", "Заголовок статьи": "", "Текст": ""} #это словарь
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

def spy_numbers_str(data):
    flag = True
    for i in data:
        if i.isdigit():
            flag = False
            break
    return flag

def spy_double_str(data):
    flag = True
    data_list = data.split('-')
    for i in data_list:
        i = i.strip() #пересохраняем строку после применения метода strip по удалению пробелов () так как строки неизменяемый тип
        if i.isalpha() == False:
            flag = False
            break    
    return flag    
#придумываем пароль: не менее 4 символов и минимум одна заглавная буква и 1 одна цифра:
# def check_password(data):
#     count1 = 0
#     count2 = 0
#     if len(data) >= 4:
#         abc = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ' + 'ZYXWVUTSRQPONMLKJIHGFEDCBA'[::-1]
#         numbers = '0123456789'
#         for i in abc:
#             count1 +=1
#             if i in data:
#                 for j in numbers:
#                     count2 +=1
#                     if j in data:
#                         print(count1, count2)
#                         return True
#     return False
# print(check_password('hjhjhj9Z'))      
              
def check_password(data):
    flag = False
    if len(data) >= 4:
        flag_letters = False
        flag_numbers = False
        flag_double = True
        for i in range(len(data)):
            if data[i].isdigit():
                flag_numbers = True
            elif pattern.search(data[i]):
                flag_letters = True
            if i < len(data) - 1:
                if data[i] == data[i + 1]:
                    # print(data[i], data[i + 1]) 
                    flag_double = False
            if  flag_letters == True and flag_numbers == True and  flag_double == True:
                flag = True
                break
    return flag





            
#
#     print(a[i])
#     if i < len(a) - 1:
#         if a[i] == a[i + 1]:
#             print(a[i], a[i + 1]) 



# print(check_password('9ZZhjhhjh99Z'))


def final_result(data):
    run = True
    while run:
        info = input(data) #data это аргумент функции final_result(data). При вызове функции final_result(data) в data попадает информация, 
        #которую должен ввести пользователь (вводит пользователь). И эта информация записывается (сохраняется) в info, 
        #иначе она нигде не сохранится после ввода пользователем. А в data хранится информация, которую мы запрашиваем у пользователя
        result_check_password = check_password(info)
        if result_check_password == False and "Введите Пароль" in data:
            continue
        result_zero = spy_zero_str(info)
        if result_zero == False:
            continue
        result_numbers = spy_numbers_str(info)
        result_double_str = spy_double_str(info)
        if (result_numbers == False or result_double_str == False) and ("Введите Фамилию" in data or "Введите Имя" in data):
            continue
        # result_double_str = spy_double_str(info)
        # if result_double_str == False and ("Введите Фамилию" in data or "Введите Имя" in data):
        #     continue
        result = spy_bad_words(info) # В result получаем информацию о том, нет ли в info (вводимых пользователем данных) плохих слов
        #  В result попадет либо True либо False
        if result == True:
            if "Введите ФИО:" in data: #если функция вызывается с аргументом, содержащим 'Введите ФИО: ', то происходит
        #запись введенных данных в словарь news с ключом ФИО
                news["Фамилия Имя"] = info
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
#записывает проверенную информацию в словари news и registration. В registration записываем Фамилию, Имя, Логин, Пароль. 
# В news записываем Введите Заголовок статьи: и Введите Текст:.
final_result('Введите Имя: ')
final_result('Введите Логин: ')
final_result('Введите Пароль: ')
print(registration)
# for i in range(3): #Запрос логина и пароля возможен 3 раза в случае неверного ввода или логина или пароля
#     login = input('Введите Логин: ')
#     password = input('Введите Пароль: ')
# # сравнить пароль и логин со словарем registration:
#     if login == registration['Логин']:
#         print(login, registration['Логин'])
#         if password == registration['Пароль']:
#             print('Добро пожаловать!')
#             break
#         else:
#             print('Логин или пароль введены неверно')
#     else:
#         print('Логин или пароль введены неверно')



# # final_result('Введите ФИО: ') 
# news['Фамилия Имя'] = registration['Фамилия'] + ' ' + registration['Имя']
# final_result('Введите Заголовок статьи: ')
# final_result('Введите Текст: ')

# current_date = datetime.datetime.now()
# # print(current_date)
# # str_current_date = str(current_date)
# # print(str(current_date))
# news["Дата"] = current_date.strftime("%d-%m-%Y")  #str_current_date[0:10]
# news["Время"] = current_date.strftime("%H:%M") #str_current_date[11:16]
# print(news)

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

file = open('database.txt', 'w')
for key in registration:
    file.write(key)
    file.write(': ')
    file.write(registration[key])
    file.write('\n')
