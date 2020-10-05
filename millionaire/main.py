import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from fetch_answer import Fetcher
from parse_question import parse, check_correct, get_possible_answer_indices


def main():
    url = 'https://education.jlab.org/million/'

    # add adblocker
    adblock_path = r'C:\Users\Dan\AppData\Local\Google\Chrome\User Data\Default\Extensions\cjpalhdlnbpafiamejdnhcphjbkeiagm\1.29.2_4'
    chrome_options = Options()
    chrome_options.add_argument('load-extension=' + adblock_path)

    # include if you don't want browser popup
    #chrome_options.add_argument('--headless')

    driver = webdriver.Chrome(options=chrome_options)
    driver.create_options()
    driver.get(url)

    fetcher = Fetcher('answers.txt')

    # click the start button
    driver.find_element_by_xpath("//div[@id='startbutton']/a").click()

    sleep_dur = 1

    level = 0

    while True:
        driver.implicitly_wait(sleep_dur)
        json = parse(driver.page_source)
        question, answers = json['question'], json['answers']

        response, guessed = fetcher.check(question, answers)
        if guessed:
            # press 5050 button
            driver.find_element_by_xpath("//img[@id='fiftyfiftybutton']").click()
            driver.implicitly_wait(sleep_dur)
            indices = get_possible_answer_indices(driver.page_source)
            #print(indices)
            response, guessed = fetcher.check(question, answers, indices)

        driver.implicitly_wait(sleep_dur)
        # click on right response
        try:
            #driver.find_element_by_xpath("//td/a[text() = '"+match+"']").click()
            driver.find_element_by_xpath("//img[@id='answer_"+str(response)+"']").click()
        except Exception as e:
            print(e)
            print(driver.find_element_by_xpath("//div[@id='answerbox']").text)
            print(answers)
            print(match)
            input('CANT FIND ERROR')
            return

        driver.implicitly_wait(sleep_dur)
        driver.find_element_by_xpath("//div[@id='finalanswer']/a").click()

        correct = check_correct(driver.page_source)

        if correct and guessed:
            fetcher.addanswer(question, answers, response)

        if correct:
            level += 1
            if level >= 15:
                input('GGs')
        else:
            # print(question)
            # print(answers)
            level = 0
            if not guessed:
                print(question)
                print(answers)
                print(response)
                input("Houston we have a problem ...")
                return

        driver.find_element_by_xpath("//div[@id='quit']/a").click()
        if not correct:
            driver.find_element_by_xpath("//div[@id='startbutton']/a").click()


    input("Done, press any key to exit ...")
    driver.quit()

if __name__ == '__main__':
    main()