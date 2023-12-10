from selenium import webdriver

URL = 'https://cuet.samarth.ac.in/index.php/app/info/universities'

def download_main_page():
    driver = webdriver.Chrome()
    driver.get(URL)
    html = driver.page_source

    with open('main_page.html','w+') as f:
        print(html,file=f)
