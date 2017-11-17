import urllib.request
import urllib.parse

""" get request """
x = urllib.request.urlopen('https://www.google.com/')
# print(x.read())

""" post request, if we need to put some date to request, for example some search request """
url = 'http://www.pythonprogramming.net'
values = {'s': 'basic', 'submit': 'search'}
data = urllib.parse.urlencode(values)
data_enc = data.encode('utf-8')
req = urllib.request.Request(url, data_enc)
resp = urllib.request.urlopen(req)
resp_data = resp.read()
print(resp_data)