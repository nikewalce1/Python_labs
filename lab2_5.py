#Введите  с  клавиатуры  текст.  Программно  найдите  в  нем  и  выведите 
#отдельно  все  слова,  которые  начинаются  с  большого  латинского 
#символа  (от  A  до  Z)  и  заканчиваются  2  или  4  цифрами,  например 
#«Petr93»,  «Johnny70»,  «Service2002».  Используйте  регулярные 
#выражения.
import re
from colorama import init
from colorama import Fore, Back, Style
init()
print(Fore.GREEN)
text = input("Write your text:")
print(text)
pattern = r'[A-Z]\D+\d{2,4}'
result = re.findall(pattern,text)
print(Fore.RED,result)
