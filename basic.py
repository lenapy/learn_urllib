import urllib.request

""" get request """
x = urllib.request.urlopen('https://www.google.com/')
print(x.read())