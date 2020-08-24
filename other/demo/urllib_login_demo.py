from urllib import request, parse
import ssl
context = ssl._create_unverified_context
url = "http://xxx/api/app_login"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
}
dict = {
    "email": "",
    "password": ""
}

data = bytes(parse.urlencode(dict), 'utf-8')

req = request.Request(url, data=data, headers=headers, method='POST')

response = request.urlopen(req, context=context)
print(response.read().decode('utf-8'))
