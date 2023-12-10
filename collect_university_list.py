from bs4 import BeautifulSoup
import json

def collect_university_list():
    with open('main_page.html','r') as f:
        page_soup = BeautifulSoup(f.read(),'html.parser')

    selector = '#searchItems > div.col-md-4 > div > div > table'

    list_soup = page_soup.select(selector)

    main_url = 'https://cuet.samarth.ac.in'

    university_list = {}

    for element in list_soup:
        tag = element.select('a')[0]
        university_list[main_url + tag.attrs['href']] = tag.contents[0].strip()
    
    with open('university_list.json','w') as f:
        json.dump(university_list,f)
