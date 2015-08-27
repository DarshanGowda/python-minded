__author__ = 'Darshan RK Gowda'

import requests
import re
from bs4 import BeautifulSoup

company_contacts = {}
response = requests.get('https://x.y.z/search.php?q=', verify=False)
raw_html = re.findall(r'<table.*>.*</table>', response.text)[0]
reformatted_html = re.sub(r'<img.*?>', '', raw_html)
soup = BeautifulSoup(reformatted_html, 'html.parser')
tr_child = soup.find_all("tr")

f = open('contacts.csv', 'w+')
f.write("Full Name, Email, Extension\n")

for index in range(1, len(tr_child), 10):
    td_childs = tr_child[index].find_all('td')
    try:
        f.write(str(td_childs[0].contents[0]).replace(",", "#") + "," + str(td_childs[1].contents[0]) + "," + str(
            td_childs[2].contents[0]) + "\n")
    except Exception as e:
        print e

f.close()

