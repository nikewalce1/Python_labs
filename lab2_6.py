#Напишите скрипт reorganize.py, который в директории --source создает 
#две  директории:  Archive  и  Small.  В  первую  директорию  помещаются 
#файлы  с  датой  изменения,  отличающейся  от  текущей  даты  на 
#количество  дней  более  параметра  --days  (т.е.  относительно  старые 
#файлы). Во вторую – все файлы размером меньше параметра --size байт. 
#Каждая  директория  должна  создаваться  только  в  случае,  если  найден 
#хотя  бы  один  файл,  который  должен  быть  в  нее  помещен.  Пример 
#вызова: 
#reorganize --source "C:\TestDir" --days 2 --size 4096 
