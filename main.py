from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from parser_nono import parse
from solver_nono import NonogramSolver


def main():
    url = 'http://www.puzzle-nonograms.com/'

    # add adblocker
    adblock_path = r'C:\Users\Dan\AppData\Local\Google\Chrome\User Data\Default\Extensions\cjpalhdlnbpafiamejdnhcphjbkeiagm\1.28.4_8'
    chrome_options = Options()
    chrome_options.add_argument('load-extension=' + adblock_path)

    driver = webdriver.Chrome(options=chrome_options)
    driver.create_options()
    #driver.implicitly_wait(30)
    driver.get(url)

    json = parse(driver.page_source)

    solver = NonogramSolver(json)
    solver.solve()
    solution = solver.result()

    #print(solver)

    # automatically click on boxes
    num_rows, num_cols = solution.shape

    grid = driver.find_element_by_xpath(
        f"//div[@class='nonograms-cell-back']"
    )

    # drag and drop functionality (maybe)
    #Actions builder = new Actions(driver);

    for r in range(num_rows):
        for c in range(num_cols):
            if solution[r][c] == 1:
                box = grid.find_element_by_xpath(
                    f".//div[{r+1}]/div[{c+1}]"
                )
                box.click()

    driver.find_element_by_xpath("//input[@id='btnReady']").click()

    input("Done, press any key to exit ...")

if __name__ == '__main__':
    main()