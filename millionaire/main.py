from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from fetch_answer import Fetcher


def main():
    url = 'https://education.jlab.org/million/'

    # add adblocker
    adblock_path = r'C:\Users\Dan\AppData\Local\Google\Chrome\User Data\Default\Extensions\cjpalhdlnbpafiamejdnhcphjbkeiagm\1.28.4_8'
    chrome_options = Options()
    chrome_options.add_argument('load-extension=' + adblock_path)

    driver = webdriver.Chrome(options=chrome_options)
    driver.create_options()
    driver.get(url)

    fetcher = Fetcher('answers.txt')

if __name__ == '__main__':
    main()