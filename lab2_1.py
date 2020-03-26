from colorama import init
from colorama import Fore, Back, Style
init()
#Напишите скрипт, который читает текстовый файл и выводит символы 
#в порядке убывания частоты встречаемости в тексте. Регистр символа 
#не  имеет  значения.  Программа  должна  учитывать  только  буквенные 
#символы  (символы  пунктуации,  цифры  и  служебные  символы  слудет 
#игнорировать).  Проверьте  работу  скрипта  на  нескольких  файлах  с 
#текстом  на  английском  и  русском  языках,  сравните  результаты  с 
#таблицами, приведенными в wikipedia.org/wiki/Letter_frequencies. 

file = open('lab2_1.txt', 'r')
lst = [text for text in file]
lst_string = ''.join(lst)#make string from list
print(Fore.GREEN, lst)
letter_in_low = [s.lower() for s in lst_string if s.isalpha()]#игнор регистр
text_letters = list(set(letter_in_low))#буквы без повторений(set)
sort_key = lambda s: letter_in_low.count(s)#лямбда-выражени работает с функцией, которая используется только в одном месте и выполняет одну единственную задачу.
text_letters.sort(key=sort_key, reverse=True)#в порядке убывания
for letter in text_letters:
    print(Fore.RED,letter, Fore.CYAN, letter_in_low.count(letter))
file.close()
if __name__ == "__main__":
	pass

# Write a script that reads a text file and displays characters
# in decreasing order of occurrence in the text. Character case
# irrelevant. The program should include only alphabetic
# characters (punctuation, numbers, and service characters
# ignore). Test the script on multiple files with
# comparative results with
# tables given in

# Напишите скрипт, который читает текстовый файл и выводит символы 
# в порядке убывания частоты встречаемости в тексте. Регистр символа 
# не  имеет  значения.  Программа  должна  учитывать  только  буквенные 
# символы  (символы  пунктуации,  цифры  и  служебные  символы  слудет 
# игнорировать).  Проверьте  работу  скрипта  на  нескольких  файлах  с 
# текстом  на  английском  и  русском  языках,  сравните  результаты  с 
# таблицами, приведенными в 
