import json
# Кодирование основных объектов Python:
json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
>>> '["foo", {"bar": ["baz", null, 1.0, 2]}]'
print(json.dumps("\"foo\bar"))
>>> "\"foo\bar"
print(json.dumps('\u1234'))
>>> "\u1234"
print(json.dumps('\\'))
>>> "\\"
print(json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True))
>>> {"a": 0, "b": 0, "c": 0}
#Компактное кодирование:
json.dumps([1,2,3,{'4': 5, '6': 7}], separators=(',', ':'))
>>> '[1,2,3,{"4":5,"6":7}]'
#Красивый вывод:
print(json.dumps({'4': 5, '6': 7}, sort_keys=True, indent=4))
{
    "4": 5,
    "6": 7
}
#Декодирование (парсинг) JSON:
json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')
>>> ['foo', {'bar': ['baz', None, 1.0, 2]}]
json.loads('"\\"foo\\bar"')
>>> '"foo\x08ar'


json.dump(obj, fp, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw) - сериализует obj как форматированный JSON поток в fp.
json.dumps(obj, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw) - сериализует obj в строку JSON-формата.
Если skipkeys = True, то ключи словаря не базового типа (str, unicode, int, long, float, bool, None) будут проигнорированы, вместо того, чтобы вызывать исключение TypeError.
Если ensure_ascii = True, все не-ASCII символы в выводе будут экранированы последовательностями \uXXXX, и результатом будет строка, содержащая только ASCII символы. Если ensure_ascii = False, строки запишутся как есть.
Если check_circular = False, то проверка циклических ссылок будет пропущена, а такие ссылки будут вызывать OverflowError.
Если allow_nan = False, при попытке сериализовать значение с запятой, выходящее за допустимые пределы, будет вызываться ValueError (nan, inf, -inf) в строгом соответствии со спецификацией JSON, вместо того, чтобы использовать эквиваленты из JavaScript (NaN, Infinity, -Infinity).
Если indent является неотрицательным числом, то массивы и объекты в JSON будут выводиться с этим уровнем отступа. Если уровень отступа 0, отрицательный или "", то вместо этого будут просто использоваться новые строки. Значение по умолчанию None отражает наиболее компактное представление. Если indent - строка, то она и будет использоваться в качестве отступа.
Если sort_keys = True, то ключи выводимого словаря будут отсортированы.

json.load(fp, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw) - десериализует JSON из fp.
json.loads(s, encoding=None, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw) - десериализует s (экземпляр str, содержащий документ JSON) в объект Python.
object_hook - опциональная функция, которая применяется к результату декодирования объекта (dict). Использоваться будет значение, возвращаемое этой функцией, а не полученный словарь.
object_pairs_hook - опциональная функция, которая применяется к результату декодирования объекта с определённой последовательностью пар ключ/значение. Будет использован результат, возвращаемый функцией, вместо исходного словаря. Если задан так же object_hook, то приоритет отдаётся object_pairs_hook.
parse_float, если определён, будет вызван для каждого значения JSON с плавающей точкой. По умолчанию, это эквивалентно float(num_str).
parse_int, если определён, будет вызван для строки JSON с числовым значением. По умолчанию эквивалентно int(num_str).
parse_constant, если определён, будет вызван для следующих строк: "-Infinity", "Infinity", "NaN". Может быть использовано для возбуждения исключений при обнаружении ошибочных чисел JSON.
Если не удастся десериализовать JSON, будет возбуждено исключение ValueError.

Ключи в парах ключ/значение в JSON всегда являются строками. Когда словарь конвертируется в JSON, все ключи словаря преобразовываются в строки. В результате этого, если словарь сначала преобразовать в JSON, а потом обратно в словарь, то можно не получить словарь, идентичный исходному. Другими словами, loads(dumps(x)) != x, если x имеет нестроковые ключи.
