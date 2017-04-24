# парсить командную строку можно двумя способами:
#   - sys.argv
#   - argparse

# http://jenyay.net/Programming/Argparse

# 1. sys.argv - самый простой способ "в лоб" распарсить командную строку
# Эффективен в самых простых случаях, считывает параметры последовательно в список, не разбираясь.
import sys

if __name__ == "__main__":
    for param in sys.argv:
        print (param)

# $ python params.py param1 param2 param3
# $ params.py
# $ param1
# $ param2
# $ param3


# 2. argparse - мощная библиотека для параметров коммандной строки

import sys
import argparse
 
 
def createParser ():
    parser = argparse.ArgumentParser(#можно запускать без параметров с ()
    	prog = 'coolprogram',
    	description = '''Это очень полезная программа, 
            которая позволяет поприветствовать нужных людей, 
            или попрощаться... со всеми.''',
        epilog = '''(c) Jenyay 2014. Автор программы, как всегда,
            не несет никакой ответственности ни за что.'''
            )) # Создаем объект класса ArgumentParser 
    """ nargs='?' - параметр не обязательный, ожидается 0 или 1 значение
    	nargs='+' - ожидается одно или более значений
        nargs=int>0 - ожидается список из int значений"""
    # обязательный, позиционный параметр, ожидаются в той же последовательности, что и объявлены
    parser.add_argument ('name', nargs='?', , default='мир', help = 'Список приветствуемых людей') 

    # именованные параметры
    parser.add_argument ('-n', '--name', '--username', default='мир', required=True) 
    # ВСЕ именованные параметры считаются НЕобязательными, если required=False (по умолчанию)
    # если значение по умолчанию не указано, то оно считается равным None
    parser.add_argument ('-n', '--name', choices=['Вася', 'Оля', 'Петя'], default='Оля') 
    # ввод только из списка значений
    # Иногда может быть полезным в качестве значения параметра choices использовать список целых чисел, 
    # полученных с помощью стандартной функции range.
    parser.add_argument ('-c', '--count', default=1, type=int) # указание типа ожидаемого параметра
    parser.add_argument ('-n', '--name', type=open) #goto 61, открытие файла. ИЛИ:
    parser.add_argument ('-n', '--name', type=argparse.FileType(mode='r', bufsize=-1, encoding=None, errors=None))

    # Флаги-параметры
    parser.add_argument ('-g', '--goodbye', action='store_const', const=True, default=False) 
    # ИЛИ (примеры идентичны)
    parser.add_argument ('-g', '--goodbye', action='store_true', default=False)

    # Несколько параметров
    # если позиционные назвать, они будут более универсальными
    # при совмещении позиционных и именованных порядок не важен

 
    return parser
 
 
if __name__ == '__main__':
    parser = createParser() #
    namespace = parser.parse_args() # встроенный метод разбора коммандной строки
 
    # print (namespace)
 
    if namespace.name:
        print ("Привет, {}!".format (namespace.name) )
    else:
        print ("Привет, мир!")

    for _ in range (namespace.count):
        print ("Привет, мир!")

    text = namespace.name.read()

