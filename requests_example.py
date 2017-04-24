import requests

r = requests.get('https://api.github.com/events')# Response object
r = requests.post("http://httpbin.org/post")
r = requests.put("http://httpbin.org/put")
r = requests.delete("http://httpbin.org/delete")
r = requests.head("http://httpbin.org/get")
r = requests.options("http://httpbin.org/get") 

# Передача параметров
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get("http://httpbin.org/get", params=payload)
print(r.url)
>>> http://httpbin.org/get?key2=value2&key1=value1

# Содержимое ответа
r.text 
u'[{"repository":{"open_issues":0,"url":"https://github.com/... }}]'
# Бинарное
r.content 
>>> b'[{"repository":{"open_issues":0,"url":"https://github.com/... }}]'
# JSON 
>>> r.json() 
[{u'repository': {u'open_issues': 0, u'url': 'https://github.com/...' }}]

# Кодировка, чтение и изменение
r.encoding
>>> 'utf-8' 
r.encoding = 'ISO-8859-1' 

#Если вы хотите добавить HTTP-заголовки в запрос, просто передайте соответствующий словарь в параметре headers.
import json
url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'} 
headers = {'content-type': 'application/json'}
r = requests.post(url, data=json.dumps(payload), headers=headers)


payload = {'key1': 'value1', 'key2': 'value2'} 
r = requests.post("http://httpbin.org/post", data=payload) 
print(r.text) 
{ ... "form": { "key2": "value2", "key1": "value1" }, ... } 


#GitHub принимает JSON-закодированные POST/PATCH данные:
import json 
url = 'https://api.github.com/some/endpoint' 
payload = {'some': 'data'}
r = requests.post(url, data=json.dumps(payload)) 

# Коды состояния
r.status_code 
200 
r.status_code == requests.codes.ok 
True

# HTTP-заголовки
r.headers {'content-encoding': 'gzip',
			'transfer-encoding': 'chunked',
			'connection': 'close',
			'server': 'nginx/1.0.4',
			'x-runtime': '148ms',
			'etag': '"e1ca502697e5c9317743dc078f67693f"',
			'content-type': 'application/json' } 

r.headers['Content-Type'] 
>>> 'application/json' 
r.headers.get('content-type') 
>>> 'application/json' 

# Cookies
# Если ответ содержит cookie, вы можете быстро получить к ним доступ:
r = requests.get(url)
r.cookies['example_cookie_name'] 
>>> 'example_cookie_value' 
#Для отправки собственных cookie на сервер, вы можете использовать параметр cookies:
cookies = dict(cookies_are='working')
r = requests.get(url, cookies=cookies) 
r.text 
>>> '{"cookies": {"cookies_are": "working"}}'


#timeout:
requests.get('http://github.com', timeout=0.001) 
#Примечание: timeout это не ограничение по времени полной загрузки ответа. 
#Исключение возникает, если сервер не дал ответ за timeout секунд 
#(точнее, если ни одного байта не было получено от основного сокета за timeout секунд).