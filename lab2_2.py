import os
import hashlib 
# Напишите скрипт, позволяющий искать в заданной директории и в ее 
# подпапках  файлы-дубликаты  на  основе  сравнени¤  контрольных  сумм 
# (MD5).  ‘айлы  могут  иметь  одинаковое  содержимое,  но  отличатьс¤ 
# именами. —крипт должен вывести группы имен обнаруженных файлов-
# дубликатов. 

path = r'E:\Python\lab2_3' 
#path = os.getcwd()
files = os.listdir(path)
filecount = []
for file in files:
    with open(path+'\\'+file, 'rb') as f:
        content = f.read()
        f.close()
        filecount.append(hashlib.md5(content).hexdigest())

for i in range(len(files) - 1):
    for j in range(i + 1, len(files)):
        if filecount[i] == filecount[j]:
            print(files[i], ' is ', files[j])

# sum_dict = {}
# for root, dirs, files in os.walk(path):
    # for file in files:
        # path = os.path.join(root, file)
        # with open(path, 'r') as f:
            # content = f.read().encode('utf-8').strip()

        # checksum = hashlib.md5(content).hexdigest()
        # if checksum in sum_dict:
            # sum_dict[checksum] += [path]
        # else:
            # sum_dict[checksum] = [path]

# sum_dict = {sum: group for sum, group in sum_dict.items() if len(group) > 1}
# counter = 1
# for group in sum_dict.values():
    # print('Group {}:'.format(counter))
    # for path in group:
        # print(path)

    # counter += 1
    # print()
