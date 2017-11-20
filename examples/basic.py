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
# print(resp_data)

""" post request with using 'User-Agent'"""
try:
    url = 'http://google.com/search?q=python'
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) " \
                            "Chrome/24.0.1312.27 Safari/537.17"
    new_req = urllib.request.Request(url, headers=headers)
    new_resp = urllib.request.urlopen(new_req)
    new_resp_data = new_resp.read()

    save_file = open('data_from_google.txt', 'w')
    save_file.write(str(new_resp_data))
    save_file.close()

except Exception as e:
    print(str(e))
