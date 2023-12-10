from download_main_page import download_main_page
from collect_university_list import collect_university_list
from scrap_universities import scrap_data

if __name__ == '__main__':
    download_main_page()
    collect_university_list()
    scrap_data()