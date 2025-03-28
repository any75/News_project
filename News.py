import datetime

BAD_WORDS = 'редиска', 'сосиска', 'репка'
news = {"ФИО": "", "Заголовок статьи": "", "Текст": ""} #это словарь
def spy_bad_words(data):
    data_list = data.split(' ')
    flag = True
    for i in data_list:
        if i.lower() in BAD_WORDS:
            print(f'Нашли плохое слово {i}')
            flag = False
            break
    return flag 
def final_result(data):
    run = True
    while run:
        info = input(data)
        result = spy_bad_words(info)
        # print(result)
        if result == True:
            if "Введите ФИО:" in data:
                news["ФИО"] = info
            elif "Введите Заголовок статьи" in data:
                news["Заголовок статьи"] = info
            elif "Введите Текст" in data:
                news["Текст"] = info
            run = False      
# date = '19.01.2025'
# time = '11:30'
# final_result('Введите ФИО: ')
# final_result('Введите Заголовок статьи: ')
# final_result('Введите Текст: ')

current_date = datetime.datetime.now()
# print(current_date)
# str_current_date = str(current_date)
# print(str(current_date))
news["Дата"] = current_date.strftime("%d-%m-%Y")  #str_current_date[0:10]
news["Время"] = current_date.strftime("%H:%M") #str_current_date[11:16]
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

