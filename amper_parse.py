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
from settings import site_url


def get_response_data(url):
    response = urllib.request.urlopen(url)
    resp_data = response.read()
    return resp_data


def get_clean_data(resp_data):
    authors = re.findall(r'<b>(.*?)</b>', str(resp_data))
    titles = re.findall(r'<u>(.*?)</u>', str(resp_data))
    mess_dates = re.findall(r'</b></a>(.*?)</span>', str(resp_data))
    clean_dates = re.findall(r'\d{1,3}/\d{1,3}/\d{1,3}', str(mess_dates))
    clean_data = zip(clean_dates, authors, titles)
    return clean_data


def save_amper_data(amper_data):
    save_data = open('t.txt', 'a')
    for data in amper_data:
        d = ', '.join(data)
        save_data.write(d)
    save_data.close()


if __name__ == '__main__':
    for n in range(1, 15):
        new_url = site_url + 'page' + str(n)
        amper_response = get_response_data(new_url)
        amper_data = get_clean_data(amper_response)
        save_amper_data(amper_data)

    with open('t.txt', 'r') as f:
        print(f.readlines())
