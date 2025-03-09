BAD_WORDS = 'редиска', 'сосиска', 'репка'
news = {} #это словарь
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
        print(result)
        if result == True:
            run = False      
date = '19.01.2025'
time = '11:30'
final_result('Введите ФИО: ')
final_result('Введите заголовок статьи: ')
final_result('Введите текст: ')
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

