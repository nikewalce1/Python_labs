import os
import re
#Задан  путь  к  директории  с  музыкальными  файлами  (в  названии 
#которых  нет  номеров,  а  только  названия  песен)  и  текстовый  файл, 
#хранящий полный список песен с номерами и названиями в виде строк 
#формата «01. Freefall [6:12]». Напишите скрипт, который корректирует 
#имена файлов в директории на основе текста списка песен. 
# path = r'D:\Programming\python\lab2_3' #os.getcwd()
# print(path)
# for root, dirs, files in os.walk(path):
	# for _files in files:
		# if _files.endswith('.com'):
			# print(_files)
# file = open('lab2_3/music.txt', 'r')
# for text in file:
	# print(text)
Play_List = {}
path_directory = r'E:\Python\lab2_3' #os.getcwd()
print(path_directory)
f= open (r'E:\Python\lab2_3\music.txt')
lines = f.readlines()
f.close()
pattern_number = r'(\d+\.\s)[\w\s-]+'
pattern_name = r'\d+\.\s([\w\s-]+)'
for line in lines:
    re_num = ''.join(re.findall(pattern_number, line))
    re_name =''.join(re.findall(pattern_name, line)).rstrip()
    Play_List[re_name] = re_num
print(Play_List)
print(os.listdir(path_directory))
for name in os.listdir(path_directory):
    if name.endswith('.mp3') and name[:-4] in Play_List :
        os.rename(name, Play_List[name[:-4]]+name)
        print('aueee')