from selenium import webdriver

from parser_nono import parse
from solver_nono import NonogramSolver


def main():
    url = 'http://www.puzzle-nonograms.com/?size=4'

    driver = webdriver.Firefox()
    #driver.implicitly_wait(30)
    #input("Press any key to start ...")
    driver.get(url)

    json = parse(driver.page_source)

    solver = NonogramSolver(json)
    solver.solve()
    solution = solver.result()

    #print(solver)

    # automatically click on boxes
    num_rows, num_cols = solution.shape

    for r in range(num_rows):
        for c in range(num_cols):
            if solution[r][c] == 1:
                box = driver.find_element_by_xpath(
                    f"//div[@class='nonograms-cell-back']/div[{r+1}]/div[{c+1}]"
                )
                box.click()


if __name__ == '__main__':
    main()