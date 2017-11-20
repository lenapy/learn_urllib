import urllib.request
import urllib.parse
import re

url = 'http://pythonprogramming.net'
values = {'s': 'basics', 'submit': 'search'}
data = urllib.parse.urlencode(values)
encode_data = data.encode('utf-8')
request = urllib.request.Request(url, encode_data)
response = urllib.request.urlopen(request)
resp_data = response.read()

paragraphs = re.findall(r'<p>(.*?)</p>', str(resp_data))  # find anything between paragraphs

for p in paragraphs:
    print(p)
