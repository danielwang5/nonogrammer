import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from scraper.state import get_state

from clicker.actions import *

def main():
    url = 'https://setwithfriends.com/'
    driver_path = r'C:\Users\Dan\Documents\side-projects\chromedriver.exe'

    chrome_options = Options()
    #chrome_options.add_argument('load-extension=' + adblock_path)

    driver = webdriver.Chrome(options=chrome_options, executable_path=driver_path)
    driver.create_options()
    driver.get(url)

    sleep_dur = 1
    while True:
        driver.implicitly_wait(sleep_dur)
        source = driver.page_source

        state = get_state(source)


if __name__ == '__main__':
    main()