import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from fetch_answer import Fetcher
from parse_question import parse, check_correct


def main():
    url = 'https://education.jlab.org/million/'

    # add adblocker
    adblock_path = r'C:\Users\Dan\AppData\Local\Google\Chrome\User Data\Default\Extensions\cjpalhdlnbpafiamejdnhcphjbkeiagm\1.29.2_4'
    chrome_options = Options()
    chrome_options.add_argument('load-extension=' + adblock_path)

    driver = webdriver.Chrome(options=chrome_options)
    driver.create_options()
    driver.get(url)

    fetcher = Fetcher('answers.txt')

    # click the start button
    driver.find_element_by_xpath("//div[@id='startbutton']/a").click()

    sleep_dur = 0.25

    while True:
        time.sleep(sleep_dur)
        json = parse(driver.page_source)
        question, answers = json['question'], json['answers']

        # print(question)
        # print(answers)

        response, guessed = fetcher.check(question, answers)
        time.sleep(sleep_dur)
        # click on right response
        driver.find_element_by_xpath("//td/a[contains(text(), '"+answers[response].split("\n")[0]+"')]").click()
        time.sleep(sleep_dur)
        driver.find_element_by_xpath("//div[@id='finalanswer']/a").click()

        correct = check_correct(driver.page_source)
        time.sleep(sleep_dur)

        if correct and guessed:
            fetcher.addanswer(question, answers, response)

        driver.find_element_by_xpath("//div[@id='quit']/a").click()
        if not correct:
            driver.find_element_by_xpath("//div[@id='startbutton']/a").click()


    input("Done, press any key to exit ...")
    driver.quit()

if __name__ == '__main__':
    main()