"""
Task:
Ampere Analysis writes a selection of blogs each week, which can all be found
on the Ampere Analysis home page (https://www.ampereanalysis.com/).Please write a short Python script that captures
the date, title and author of all blog posts on the Ampere website,
and either prints them out or returns them as a CSV or TSV file.
A sample output of a few blog posts might look like the following:

Date, Author, Title
14/06/17, Toby Holleran, VMSO on the Horizon for Verizon
6/06/2017, Alex Varatharajah, Flexible Bundling retains TV Season value
2/06/2017, Guy Bisson, ANGACOM: Content comes back to Cable
"""

import urllib.request
import re

url = 'https://www.ampereanalysis.com/'
response = urllib.request.urlopen(url)
resp_data = response.read()
authors = re.findall(r'<b>(.*?)</b>', str(resp_data))
titles = re.findall(r'<u>(.*?)</u>', str(resp_data))
mess_dates = re.findall(r'</b></a>(.*?)</span>', str(resp_data))
clean_dates = re.findall(r'\d{1,3}/\d{1,3}/\d{1,3}', str(mess_dates))


parse_data = zip(clean_dates, authors, titles)
save_data = open('parse_data.txt', 'w')
for data in parse_data:
    d = ','.join(data)
    save_data.write(d)
save_data.close()
