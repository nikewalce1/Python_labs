import os
from glob import glob
import os.path
#Задан  путь  к  директории  с  музыкальными  файлами  (в  названии 
#которых  нет  номеров,  а  только  названия  песен)  и  текстовый  файл, 
#хранящий полный список песен с номерами и названиями в виде строк 
#формата «01. Freefall [6:12]». Напишите скрипт, который корректирует 
#имена файлов в директории на основе текста списка песен. 
path = "E:\\Python\\lab2_3"
os.chdir(path)

# trackFiles = list(filter(None, [None if i == 'fileLists.txt' else i for i in os.listdir(path)]))
trackFiles = glob('*.mp3')

namesFiles = list(filter(None, [text.replace('\n', '') if text is not 'fileLists.txt' else None for text in
                                open('music.txt', 'r', encoding='UTF-8')]))

cnt = 0
Done = False

for i in range(len(trackFiles)):
    try:
        os.rename(trackFiles[i], namesFiles[i])
        if cnt == len(trackFiles) - 1:
            Done = True
        cnt += 1
    except Exception as e:
        print('Some error with file #' + str(cnt) + ': ', e.args)

if Done:
    print('All files renamed!')
else:
    print('oh shit, here we got some errors!')
    
    
# Play_List = {}
# path_directory = r'E:\Python\lab2_3' #os.getcwd()
# print(path_directory)
# f= open (r'E:\Python\lab2_3\music.txt')
# lines = f.readlines()
# f.close()
# pattern_number = r'(\d+\.\s)[\w\s-]+'
# pattern_name = r'\d+\.\s([\w\s-]+)'
# for line in lines:
    # re_num = ''.join(re.findall(pattern_number, line))
    # re_name =''.join(re.findall(pattern_name, line)).rstrip()
    # Play_List[re_name] = re_num
# print(Play_List)
# print(os.listdir(path_directory))
# for name in os.listdir(path_directory):
    # if name.endswith('.mp3') and name[:-4] in:
        # os.rename(name, Play_List[name[:-4]]+name)
        # print('eee')
