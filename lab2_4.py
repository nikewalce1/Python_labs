import re
from colorama import init
from colorama import Fore, Back, Style
init()
# #Nапишите  скрипт,  который  позволяет  ввести  с  клавиатуры  имя 
# #текстового файла, найти в нем с помощью регулярных выражений все 
# #подстроки определенного вида, в соответствии с вариантом.
# #Вариант 1: найдите все даты – подстроки вида «11-05-2014». 


path = open('lab2_4.txt', 'r')
lines = path.readlines()
pattern = r'\d\d-\d\d-\d\d\d\d+'
count = 0
for line in lines:
    count+=1
    date = re.findall(pattern, line)
    if date:
        for new_date in date:
            print('Строка {0}, позиция {1} : найдено {2}'.format(count, line.index(new_date), new_date))

