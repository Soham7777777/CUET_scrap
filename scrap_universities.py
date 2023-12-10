import pandas
import sqlite3
import json
from selenium import webdriver
from time import sleep
from io import StringIO

# total 251 universities
def scrap_data():
    with open('university_list.json','r') as f:
        university_list = json.load(f)

    driver = webdriver.Chrome()
    connection = sqlite3.connect('Universities_database.sqlite')   

    i=0
    for url,name in list(university_list.items())[1:]:
        driver.get(url)
        page = driver.page_source
        table = pandas.read_html(StringIO(page))[0]
        table.to_sql(name+str(i),connection,if_exists='replace')
        sleep(2)
        i += 1
        
    connection.close()