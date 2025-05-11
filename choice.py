file = open('database.txt', 'r')
a = int(input("Что Вы планируете делать? Введите: 1 - Зарегистрироваться 2 - Авторизоваться\n"))
if a == 1:
    print('Регистрация')
elif a == 2:
    print('Авторизация')
else:
    print('Ошибка')
database = {}
for i in file:
    if i != '':
        #print(i, end='')
        b = i.split(': ')
        print(b)
        database[b[0]] = b[1]    
    print(database)
