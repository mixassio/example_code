# Открытие файла
f = open('text.txt', 'r')
# 'r'	открытие на чтение (является значением по умолчанию).
# 'w'	открытие на запись, содержимое файла удаляется, если файла не существует, создается новый.
# 'x'	открытие на запись, если файла не существует, иначе исключение.
# 'a'	открытие на дозапись, информация добавляется в конец файла.
# 'b'	открытие в двоичном режиме.
# 't'	открытие в текстовом режиме (является значением по умолчанию).
# '+'	открытие на чтение и запись

# Чтение из файла
f = open('text.txt')
f.read(1)
'H'
f.read()
'ello world!\nThe end.\n\n'

f = open('text.txt')
for line in f:
    print(line)
'Hello world!\n'
'\n'
'The end.\n'
'\n'
# Запись в файл
l = [1, 2, 34, 567, 8901]
f = open('text.txt', 'w')
for index in l:
    f.write(index + '\n')
1
1
2
3
4
# Закрытие файла
f.close()

# Функция по загрузке списка значений из файла в список
def load_list_into_file(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r') as file_text:
            list_url = [line.strip() for line in file_text]
    return list_url


# Функция для загрузки при сложных случаях, выдаёт стринг или жсон
def load_data(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'rb') as file_text:
            char_type = chardet.detect(file_text.read())['encoding']
        with codecs.open(filepath, 'rb', encoding=char_type) as file_text:
            return file_text.read() # ИЛИ
            return json.load(file_json)
