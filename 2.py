'''
10.
а) Дан файл f, компоненти якого є цілими числами. Отримати в файлі g всі
компоненти файлу f що є простими числами. Простим називається число, що більше за 1
та не має інших дільників, окрім 1 та самого себе)
Серебренников
''' 
a=open('a.txt', 'w')#открываем файл в режиме записи
e=input('Write in English please: ')#пишим предложение
a.write(e)#записываем его
a=open('a.txt', 'r')#в реж. чтения
b=list(a.read())#сбор информации с него
d=['a','o','u','e','i']#гласные
for c in b:#условие
    if c=='a' or  c=='o' or c=='u' or c=='e' or c=='i':
        try:
            d.remove(c)# удалаем с этого списка те которые не воли в изначальное предложение
        except:
            True#Избежаение повторений
a=open('a.txt', 'w')#записываем ещё раз
a.write(e)#
a.write(str(d))#

a=open('a.txt', 'r')#чтение
