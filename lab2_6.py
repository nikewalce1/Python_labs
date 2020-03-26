#Напишите скрипт reorganize.py, который в директории --source создает 
#две  директории:  Archive  и  Small.  В  первую  директорию  помещаются 
#файлы  с  датой  изменения,  отличающейся  от  текущей  даты  на 
#количество  дней  более  параметра  --days  (т.е.  относительно  старые 
#файлы). Во вторую – все файлы размером меньше параметра --size байт. 
#Каждая  директория  должна  создаваться  только  в  случае,  если  найден 
#хотя  бы  один  файл,  который  должен  быть  в  нее  помещен.  Пример 
#вызова: 
#reorganize --source "C:\TestDir" --days 2 --size 4096 
import os
import datetime
import shutil

example = 'reorganize --source "TestDir" --days 2 --size 4096'
time_dir = os.path.join('--source', 'Small')
size_dir = os.path.join('--source', 'Archive')
comands = example.split()
print(comands)
days = int(comands[4])
size = int(comands[6])
print(days, size)
dir_name = comands[2]
dir_name = dir_name[1:-1]
print(dir_name)
term = datetime.timedelta(days)
cur_time = datetime.datetime.today()
for name in os.listdir(dir_name):
    path = os.path.join(dir_name, name)
    if os.path.getsize(path) > size and os.path.isfile(path):
        if not os.path.exists(size_dir):            
            os.makedirs(size_dir)
        shutil.copy(path, os.path.join(size_dir, os.path.basename(name)))
    creation_time = datetime.datetime.fromtimestamp(os.path.getmtime(path))
    if creation_time + term < cur_time and os.path.isfile(path):
        if not os.path.exists(time_dir):
            os.makedirs(time_dir)
        shutil.copy(path, os.path.join(time_dir, os.path.basename(name)))
print('End copy')

