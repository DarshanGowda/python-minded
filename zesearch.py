__author__ = 'Darshan RK Gowda'

import requests
from bs4 import BeautifulSoup

response = requests.get('https://x.y.z/search.php?q=', verify=False)
soup = BeautifulSoup(response.text, 'lxml')  # use lxml to scan even broken html
basic_info = {}

for each_div in soup.findAll('div', onclick=True):
    basic_info_tag = each_div.findPrevious(name='tr')
    basic_info_tag_childs = basic_info_tag.find_all('td')

    emp_name = basic_info_tag_childs[1].text  # scaning basic info
    if emp_name:
        basic_info[emp_name] = {"name": basic_info_tag_childs[0].text,
                                "extn": basic_info_tag_childs[2].text}

        reportees_tags = basic_info_tag.next_sibling.findAll(class_="myclass")  # scanning more info
        reporter_name = reportees_tags[0].attrs['rel']
        basic_info[emp_name]['reportees'] = "#".join(reportees_tags[1].text.split(','))
        basic_info[emp_name]['reportingTo'] = reporter_name

with open('contacts.csv', 'w') as fd:
    fd.write("Full Name, Email, Extension, reportees, reportingTo\n")
    for email, info in basic_info.items():
        try:
            fd.write(",".join([info['name'], email, info['extn'], info['reportees'], info['reportingTo']]).encode(
                'utf-8') + "\n")
        except Exception as e:
            print e
